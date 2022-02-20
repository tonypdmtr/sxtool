################################################################################
# Makefile (Borland MAKE) for building SXTOOL.EXE
################################################################################

HELP:
 @echo "*********************************************************
 @echo "* Targets : ALL SXTOOL.EXE
 @echo "*********************************************************
 @echo "* Defines:
 @echo "*********************************************************

################################################################################

all: sxtool.exe

PYTHON   = c:/python

C_LIST =   sxtool.c \
           src\const.c \
           src\data_table.c \
           src\form_insert_row_value.c \
           src\form_set_row_size.c \
           src\form_split_item.c \
           src\gui\ui_form_insert_row_value.c \
           src\gui\ui_form_set_row_size.c \
           src\gui\ui_form_split_item.c \
           src\gui\ui_insert_dialog.c \
           src\gui\ui_main_form.c \
           src\gui\ui_paste_dialog.c \
           src\gui\ui_to_py.c \
           src\gui\ui_xor_dialog.c \
           src\gui\__init__.c \
           src\insert_dialog.c \
           src\main_form.c \
           src\paste_dialog.c \
           src\sx_file.c \
           src\sx_item.c \
           src\utils.c \
           src\xor_dialog.c \
           src\__init__.c

.py.c:
 $(PYTHON)/scripts/cython -3 --embed $**

sxtool.exe: $(C_LIST)
 c:/vc/bin/cl.exe $(C_LIST) -I$(PYTHON)/include -link $(PYTHON)/libs/python38.lib
