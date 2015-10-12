# mtk-ota-update-preloader-lk

Automatic generate preloader/lk/logo/trustzone update for OTA delta package for MTK from ota package file.


#Step 1, Modify build/core/Makefile

You need first build the image into ota package, to do this, modfiy build/core/Makefile, for BUILT_TARGET_FILES_PACKAGE, adding :

$(hide)	mkdir -p $(zip_root)/MTK_RADIO
$(hide) $(ACP) $(PRODUCT_OUT)/unsigned-image/trustzone.bin $(zip_root)/MTK_RADIO/trustzone.bin
$(hide) $(ACP) $(INSTALLED_UBOOTIMAGE_TARGET) $(zip_root)/MTK_RADIO/lk.bin
$(hide) $(ACP) $(INSTALLED_PRELOADER_TARGET) $(zip_root)/MTK_RADIO/preloader.bin
$(hide) $(ACP) $(INSTALLED_LOG_TARGET) $(zip_root)/MTK_RADIO/logo.bin

NOTE: You may need a little modification based on different MTK platforms.


#Step 2, when generate package, adding -s to use this releasetools.py.

ota_from_target_fils -s releasetools.py -k .... -i <source> <target> delta.zip
