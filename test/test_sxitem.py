#!/usr/bin/env python

# Copyright 2018 Philippe Fremy
# This software is provided under the BSD 2 clause license; see LICENSE.txt file for more information

import unittest, io, sys, os

sys.path.append( os.path.join( os.path.dirname(__file__), '..' ) )
from src.sx_item import *
from src.form_insert_row_value import FormInsertRowValue

s = 'S1130000285F245F2212226A000424290008237C2A'


class TestUtils( unittest.TestCase ) :
    def testStr2hex(self):
        self.assertEqual( str2hex(''), [])
        self.assertEqual( str2hex(None), [])
        self.assertEqual( str2hex('1234'), [0x12, 0x34] )
        self.assertEqual( str2hex('\t12 34\n56'), [0x12, 0x34, 0x56])
        self.assertRaises( ValueError, str2hex, '1')

    def testHex2str(self):
        self.assertEqual( hex2str( [0x12, 0x34] ), '1234' )
        self.assertRaises( ValueError, hex2str, [0x100, 0x34] )
        self.assertEqual( hex2str([]), '' )

    def testStr2hexi( self ):
        self.assertEqual( str2hexi( 'FF'), 0xFF )
        self.assertEqual( str2hexi( ''), 0 )
        self.assertEqual( str2hexi( 'F'), 0xF )

    def testToHexLen(self):
        def testToHexLenSingle(expected, number, length):
            r = toHexLen(number, length)
            if r != expected:
                print( "FAIL toHexLen(%s, %d) \t= %s\t%s" % (str(number), length, r, s) )
            self.assertEqual( r, expected )

        testToHexLenSingle("1", 1, 1)
        testToHexLenSingle("01", 1, 2)
        testToHexLenSingle("012", 0x12, 3)
        testToHexLenSingle("112", 0x112, 3)
        testToHexLenSingle("002A", 0x2A, 4)
        testToHexLenSingle("000001", 1, 6)
        
        testToHexLenSingle("1", "0x01", 1)
        testToHexLenSingle("01", "0x01", 2)
        testToHexLenSingle("2A", "2A", 2)
        testToHexLenSingle("002A", "2A", 4)
        testToHexLenSingle("002A", "0x2A", 4)
        
        testToHexLenSingle("2A", 42, 2)
        testToHexLenSingle("02A", 42, 3)
        
        testToHexLenSingle("22", "22", 2)
        testToHexLenSingle("22", "0022", 2)
        testToHexLenSingle("22", "000022", 2)
        testToHexLenSingle("0022", "22", 4)
        testToHexLenSingle("0022", "0022", 4)
        testToHexLenSingle("0022", "000022", 4)
        testToHexLenSingle("000022", "22", 6)
        testToHexLenSingle("000022", "0022", 6)
        testToHexLenSingle("000022", "000022", 6)
        
        # Test reducing string with modulo 2^(length/2*8)
        testToHexLenSingle("11", "2211", 2)
        testToHexLenSingle("11", "222211", 2)

    def testXor(self):
        self.assertEqual( xor('0F', '1E'), '11')
        self.assertEqual( xor('1F',  'E'), 'FF')
        self.assertRaises( ValueError, xor, 'F', '1F')



class TestSxItem( unittest.TestCase ) :

    def testSxItemCreationError( self ):
        self.assertRaises( ValueError, SxItem, 'SX', '13', '0000', '285F245F2212226A000424290008237C', 'FF' )

    def testFormatAddress( self ):
        self.assertEqual( SxItem.formatAddress(0x1234, 'S0'), '1234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S0'), '0034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S5'), '1234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S5'), '34' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S1'), '1234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S1'), '0034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S9'), '1234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S9'), '0034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S2'), '001234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S2'), '000034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S8'), '001234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S8'), '000034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S3'), '00001234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S3'), '00000034' )

        self.assertEqual( SxItem.formatAddress(0x1234, 'S7'), '00001234' )
        self.assertEqual( SxItem.formatAddress(0x34, 'S7'), '00000034' )

    def testChecksum( self ):
        sx = SxItem( 'S1', '13', '0000', '285F245F2212226A000424290008237C', 'FF' )
        sx.updateChecksum()
        self.assertEqual( sx.checksum, '2A' )

    def testDataQuantity( self ):
        sx = SxItem( 'S1', 'FF', '0000', '285F245F2212226A000424290008237C', '2A' )
        sx.updateDataQuantity()
        self.assertEqual( sx.data_quantity, '13' )

    def testData( self ):
        sx = SxItem( 'S1', 'FF', '0000', '285F245F2212226A00042429000823', '2A' )
        sx.updateData( '285F245F2212226A000424290008237C' )
        self.assertEqual( sx.data_quantity, '13' )
        self.assertEqual( sx.checksum, '2A' )

    def testAddress( self ):
        sx = SxItem( 'S1', '13', 'FFFF', '285F245F2212226A000424290008237C', 'FF' )
        sx.updateAddress( '0000' )
        self.assertEqual( sx.data_quantity, '13' )
        self.assertEqual( sx.checksum, '2A' )

    def testRepr( self ):
        sx = SxItem( 'S1', '05', '4321', '1122', '33' )
        self.assertEqual( str(sx) , 'S1054321112233' )

        sx = SxItem( 'S2', '06', '654321', '1122', '33' )
        self.assertEqual( str(sx) , 'S206654321112233' )

        sx = SxItem( 'S3', '07', '87654321', '1122', '33' )
        self.assertEqual( str(sx) , 'S30787654321112233' )

        sx = SxItem( 'S5', '03', '4321', '', '33' )
        self.assertEqual( str(sx) , 'S503432133' )

        sx = SxItem( 'S0', '03', '4321', '', '33' )
        self.assertEqual( str(sx) , 'S003432133' )


    def testConvertAndRepr( self ):
        ref_s19 = 'S1130000285F245F2212226A000424290008237C2A'
        ref_s28 = 'S214000000285F245F2212226A000424290008237C29'
        ref_s37 = 'S31500000000285F245F2212226A000424290008237C28'
        ref_s91 = 'S9031122C9'
        ref_s82 = 'S804001122C8'
        ref_s73 = 'S70500001122C7'
        ref_s55 = 'S5031122FF'
        ref_s00 = 'S004000088FF'

        # S1 to S1, S2, S3
        sx = SxItem( 'S1', '13', '0000', '285F245F2212226A000424290008237C', '2A' )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s28 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s37 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )

        # S2 to S1, S2, S3
        sx.setContent( ref_s28 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s28 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s37 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )

        # S3 to S1, S2, S3
        sx.setContent( ref_s37 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s28 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s37 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s19 )

        # S7 to S7, S8, S9
        sx.setContent( ref_s73 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s82 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s73 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )

        # S8 to S7, S8, S9
        sx.setContent( ref_s82 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s82 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s73 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )

        # S9 to S7, S8, S9
        sx.setContent( ref_s91 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )
        sx.convert('S28')
        self.assertEqual( str(sx), ref_s82 )
        sx.convert('S37')
        self.assertEqual( str(sx), ref_s73 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s91 )

        # S5 remains S5
        sx.setContent( ref_s55 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s55 )
        sx.convert('S28')
        self.assertEqual( str(sx) , ref_s55 )
        sx.convert('S37')
        self.assertEqual( str(sx) , ref_s55 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s55 )

        # S0 remains S0
        sx.setContent( ref_s00 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s00 )
        sx.convert('S28')
        self.assertEqual( str(sx) , ref_s00 )
        sx.convert('S37')
        self.assertEqual( str(sx) , ref_s00 )
        sx.convert('S19')
        self.assertEqual( str(sx) , ref_s00 )


    def testSetContent(self):
        ref_s19 = 'S1130000285F245F2212226A000424290008237C2A'
        sx = SxItem('','','','','')
        sx.setContent( ref_s19 )
        sx.updateChecksum()
        self.assertEqual( sx.format, 'S1' )
        self.assertEqual( sx.data_quantity, '13' )
        self.assertEqual( sx.checksum, '2A' )

        ref_s28 = 'S214000000285F245F2212226A000424290008237C29'
        sx.setContent( ref_s28 )
        sx.updateChecksum()
        self.assertEqual( sx.format, 'S2' )
        self.assertEqual( sx.data_quantity, '14' )
        self.assertEqual( sx.checksum, '29' )

        ref_s37 = 'S31500000000285F245F2212226A000424290008237C28'
        sx.setContent( ref_s37 )
        sx.updateChecksum()
        self.assertEqual( sx.format, 'S3' )
        self.assertEqual( sx.data_quantity, '15' )
        self.assertEqual( sx.checksum, '28' )

        self.assertRaises( SxItemBadFileFormat, sx.setContent, 'SX1234' )

    def testSplit( self ):
        sdata = 'S1090123112233445566FF'
        sx = SxItem( '', '', '', '', '' )
        sx.setContent( sdata )

        self.assertRaises( SxItemBadOffset, sx.split, 0 )
        self.assertRaises( SxItemBadOffset, sx.split, 6 )

        sx2 = sx.split(2)

        self.assertEqual( sx.address, '0123' )
        self.assertEqual( sx.data,    '1122' )
        self.assertEqual( sx.data_quantity, '05' )

        self.assertEqual( sx2.address, '0125' )
        self.assertEqual( sx2.data,    '33445566' )
        self.assertEqual( sx2.data_quantity, '07' )

        self.assertRaises( SxItemBadOffset, sx.split, 2 )

    def testMergePossible( self ):
        sdata = 'S1090123112233445566FF'
        sx = SxItem( '', '', '', '', '' )
        sx.setContent( sdata )
        sx2 = sx.split(2)

        sx2.address = '0124'
        self.assertEqual( sx.mergePossible( sx2 ), False )

        sx2.address = '0125'
        self.assertEqual( sx.mergePossible( sx2 ), True )
        sx.merge( sx2 )

    def testMerge( self ):
        sdata = 'S1090123112233445566FF'
        sx = SxItem( '', '', '', '', '' )
        sx.setContent( sdata )
        sx2 = sx.split(2)

        sx2.address = '0124'
        self.assertRaises( SxItemBadNewAddress, sx.merge, sx2 )

        sx2.address = '0125'
        sx.merge( sx2 )

        self.assertEqual( sx.address, '0123' )
        self.assertEqual( sx.data,    '112233445566' )
        self.assertEqual( sx.data_quantity, '09' )

    def testApplyNewRowSize( self ):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0123', '111213', 'FF' ),
            SxItem( 'S1', '03', '0126', '212223', 'FF' ),
            SxItem( 'S1', '03', '0129', '313233', 'FF' ),
            SxItem( 'S1', '03', '012C', '414243', 'FF' ),
        ]

        sxfile.applyNewRowSize( 2, 1 ,3 )

        self.assertEqual( sxfile.sxItems[0].data, '010203' )
        self.assertEqual( sxfile.sxItems[1].data, '1112' )
        self.assertEqual( sxfile.sxItems[2].data, '1321' )
        self.assertEqual( sxfile.sxItems[3].data, '2223' )
        self.assertEqual( sxfile.sxItems[4].data, '3132' )
        self.assertEqual( sxfile.sxItems[5].data, '33' )


    def testFlipBits(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0123', '111213', 'FF' ),
            SxItem( 'S1', '03', '0126', '212223', 'FF' ),
            SxItem( 'S1', '03', '0129', '313233', 'FF' ),
            SxItem( 'S1', '03', '012C', '414243', 'FF' ),
        ]
        for item in sxfile.sxItems :
            item.flipBits()
        self.assertEqual(sxfile.sxItems[0].data, 'FEFDFC')
        self.assertEqual(sxfile.sxItems[1].data, 'EEEDEC')
        self.assertEqual(sxfile.sxItems[2].data, 'DEDDDC')
        self.assertEqual(sxfile.sxItems[3].data, 'CECDCC')
        self.assertEqual(sxfile.sxItems[4].data, 'BEBDBC')
        
    def testApplyOffset(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0123', '111213', 'FF' ),
            SxItem( 'S1', '03', '0126', '212223', 'FF' ),
            SxItem( 'S1', '03', '0129', '313233', 'FF' ),
            SxItem( 'S1', '03', '012C', '414243', 'FF' ),
        ]
        i = 1
        for item in sxfile.sxItems :
            item.applyOffset(i)
            i += 5
        self.assertEqual(sxfile.sxItems[0].address, '0124')
        self.assertEqual(sxfile.sxItems[1].address, '0129')
        self.assertEqual(sxfile.sxItems[2].address, '0131')
        self.assertEqual(sxfile.sxItems[3].address, '0139')
        self.assertEqual(sxfile.sxItems[4].address, '0141')
    
    def testXorData(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0123', '111213', 'FF' ),
            SxItem( 'S1', '03', '0126', '212223', 'FF' ),
            SxItem( 'S1', '03', '0129', '313233', 'FF' ),
            SxItem( 'S1', '03', '012C', '414243', 'FF' ),
        ]
        for item in sxfile.sxItems :
            item.xorData('15AF')
        self.assertEqual(sxfile.sxItems[0].data, '14AD03')
        self.assertEqual(sxfile.sxItems[1].data, '04BD13')
        self.assertEqual(sxfile.sxItems[2].data, '348D23')
        self.assertEqual(sxfile.sxItems[3].data, '249D33')
        self.assertEqual(sxfile.sxItems[4].data, '54ED43')


class TestSxFile(unittest.TestCase):

    def testDeleteEmptySxFile(self):
        sxf = SxFile()
        del sxf

    def testDeleteFullSxFile(self):
        mys = '''S00A11223344556677889900
S10B00000001020304050607FF
S10B000808090A0B0C0D0E0FFF
S90300000F
'''
        sxf = SxFile()
        fstream = io.StringIO(mys)  # type: TextIO
        sxf.fromFileStream( fstream, 'stream')
        del sxf

    def testSxFileSplitItem(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0123', '111213', 'FF' ),
            SxItem( 'S1', '03', '012C', '212223', 'FF' ),
        ]

        sxfile.splitItem( 1, 2 )

        self.assertEqual( sxfile.sxItems[0].data, '010203' )
        self.assertEqual( sxfile.sxItems[1].data, '1112' )
        self.assertEqual( sxfile.sxItems[2].data, '13' )
        self.assertEqual( sxfile.sxItems[3].data, '212223' )

        
    def testSxFileMergeItem(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0126', '111213', 'FF' ),
            SxItem( 'S1', '03', '0129', '212223', 'FF' ),
            SxItem( 'S1', '03', '012C', '313233', 'FF' ),
            SxItem( 'S1', '03', '012F', '414243', 'FF' ),
        ]

        sxfile.mergeItem( 1, 3 )

        self.assertEqual( sxfile.sxItems[0].data, '010203' )
        self.assertEqual( sxfile.sxItems[1].data, '111213212223313233' )
        self.assertEqual( sxfile.sxItems[2].data, '414243' )

        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0126', '111213', 'FF' ),
            SxItem( 'S1', '03', '0123', '212223', 'FF' ),
            SxItem( 'S1', '03', '0126', '313233', 'FF' ),
            SxItem( 'S1', '03', '0129', '414243', 'FF' ),
        ]

        sxfile.mergeItem( 1, 3 )

        self.assertEqual( sxfile.sxItems[0].data, '010203' )
        self.assertEqual( sxfile.sxItems[1].data, '111213' )
        self.assertEqual( sxfile.sxItems[2].data, '212223313233' )
        self.assertEqual( sxfile.sxItems[3].data, '414243' )

    def testSxFileLoadSave(self):
        sxFile = SxFile()
        fnames = ['example1.s19', 'example2.s19', 'example3.s28', 'example4.s37', 'example5.s19']
        for fname in fnames:
            sxFile.fromFile(fname)
            with open(fname) as f:
                refOut = f.read().strip()
            strOut = io.StringIO()
            sxFile.toFileStream(strOut)
            self.assertEqual(strOut.getvalue().strip(), refOut)
            strOut.close()

    def testGetFormat(self):
        sxFile = SxFile()
        self.assertEqual( sxFile.getFormat(), '')
        fnamesAndFmt = [('example1.s19','s19'), ('example2.s19','s19'), ('example3.s28','s28'), ('example4.s37','s37'), ('example5.s19','s19')]
        for fname,fmt in fnamesAndFmt:
            with self.subTest(fname):
                sxFile.fromFile(fname)
                self.assertEqual( sxFile.getFormat(), fmt)

    def testSxFileRepr(self):
        sxfile = SxFile()
        sxfile.sxItems = [ 
            SxItem( 'S1', '03', '0123', '010203', 'FF' ),
            SxItem( 'S1', '03', '0126', '111213', 'FF' ),
        ]
        self.assertEqual(str(sxfile), '''
S1030123010203FF
S1030126111213FF

''')

    def testUpdateDataRange(self):
        sxfile = SxFile()
        sin = '\n'.join( [
            'S004000088FF',
            'S1' '06' '0123' '010203' 'FF',
            'S1' '06' '0126' '111213' 'FF',
            'S1' '06' '0129' '212223' 'FF',
            'S1' '06' '012C' '313233' 'FF',
            'S1' '06' '012F' '414243' 'FF'
        ] )
        sxfile.fromFileStream( io.StringIO(sin), 'stream' )

        self.assertEqual(str(sxfile), '''S004000088FF
S1060123010203FF
S1060126111213FF
S1060129212223FF
S106012C313233FF
S106012F414243FF
''' )

        sxfile.updateDataRange('AABB', (1,4))
        self.assertEqual(str(sxfile), '''S004000088FF
S1060123010203FF
S1050126AABB6E
S1050129AABB6B
S105012CAABB68
S106012F414243FF
''' )


    def testConvertRange(self):
        sxfile = SxFile()
        sin = '\n'.join( [
            'S004000088FF',
            'S1' '06' '0123' '010203' 'FF',
            'S1' '06' '0126' '111213' 'FF',
            'S1' '06' '0129' '212223' 'FF',
            'S1' '06' '012C' '313233' 'FF',
            'S1' '06' '012F' '414243' 'FF'
        ] )
        sxfile.fromFileStream( io.StringIO(sin), 'stream' )
        self.assertEqual(str(sxfile), '''S004000088FF
S1060123010203FF
S1060126111213FF
S1060129212223FF
S106012C313233FF
S106012F414243FF
''' )

        sxfile.convertRange('S28', (1,4))
        self.assertEqual(str(sxfile), '''S004000088FF
S1060123010203FF
S2070001261112139B
S20700012921222368
S20700012C31323335
S106012F414243FF
''' )



class TestAdjustAddressLength(unittest.TestCase):

    def testAdjustAddressLength(self):
        self.assertEqual( FormInsertRowValue.adjustAddressLength( FormInsertRowValue, '12', 'S19'), '0012' )
        self.assertEqual( FormInsertRowValue.adjustAddressLength( FormInsertRowValue, '1', 'S19'), '0001' )
        self.assertEqual( FormInsertRowValue.adjustAddressLength( FormInsertRowValue, '12345', 'S19'), '2345' )
        self.assertEqual( FormInsertRowValue.adjustAddressLength( FormInsertRowValue, '', 'S19'), '0000' )

if __name__ == "__main__":
    unittest.main()
    # main( testRunner = TextTestRunner( verbosity = 2 ) )
