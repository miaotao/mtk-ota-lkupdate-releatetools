"""
miaotao1@gmail.com

(installing the preloader/trustzone/logo/uboot image)."""

import common
import re
import tempfile


class BinaryFileCompare:
	def __init__(self,info,fileinzip):
		self.path = fileinzip
		self.info = info
		self.source_data = self._readZip(info.source_zip, fileinzip)
		self.target_data = self._readZip(info.target_zip, fileinzip)

	def _readZip(self,zipfile,fileinzip):
		if fileinzip in zipfile.namelist():
			return zipfile.read(fileinzip)
		return None

	def needOta(self):
		return  self.source_data != self.target_data and self.target_data != None
		#return self.target_data != None

	def getTargetBinaryFile(self):
		tf = tempfile.NamedTemporaryFile(prefix='MTK_RADIO', suffix='.bin', delete=False)
		tf.write(self.target_data)
		tf.flush()
		tf.close()
		common.OPTIONS.tempfiles.append(tf.name)
		return tf.name
		


def IncrementalOTA_TrigerMtkUpdateOption(info):
	#Preloader
	cp = BinaryFileCompare(info, "MTK_RADIO/preloader.bin")
	if cp.needOta():
		print "[MTK_RADIO] adding preloader"
		common.OPTIONS.preloader = cp.getTargetBinaryFile()

	#lk
	cp = BinaryFileCompare(info, "MTK_RADIO/lk.bin")
	if cp.needOta():
		print "[MTK_RADIO] adding lk"
		common.OPTIONS.uboot = cp.getTargetBinaryFile()

	#logo
	cp = BinaryFileCompare(info, "MTK_RADIO/logo.bin")
	if cp.needOta():
		print "[MTK_RADIO] adding logo"
		common.OPTIONS.logo = cp.getTargetBinaryFile()

	#trustzone
	cp = BinaryFileCompare(info, "MTK_RADIO/trustzone.bin")
	if cp.needOta():
		print "[MTK_RADIO] adding trustzone"
		common.OPTIONS.trustzone = cp.getTargetBinaryFile()


def FullOTA_Assertions(info):
	return


def IncrementalOTA_Assertions(info):
	'''
	Trick here, we just prepare the file and set options, 
	'''
	print "[MTK_RADIO] calling IncrementalOTA_Assertions"
	IncrementalOTA_TrigerMtkUpdateOption(info)
	return


def IncrementalOTA_VerifyEnd(info):
 return



def FullOTA_InstallEnd(info):
  return



def IncrementalOTA_InstallEnd(info):
  return
