print(__file__)

# EPICS area detector(s)

from ophyd import SingleTrigger, AreaDetector, SimDetector
from ophyd import HDF5Plugin
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component, Device, EpicsSignalWithRBV
from ophyd.areadetector import ADComponent


class MyHDF5Plugin(HDF5Plugin, FileStoreHDF5IterativeWrite):
	
	file_number_sync = None
	
	def get_frames_per_point(self):
		return self.parent.cam.num_images.get()
	

class MySimDetector(SingleTrigger, SimDetector):
	
	hdf1 = Component(
		MyHDF5Plugin, 
		"HDF1:", 
		root="/", 			# for databroker filestore
		write_path_template="/tmp",	# for EPICS area detector
		fs=fs,
		)


#simdet = MySimDetector('13SIM1:', name='simdet')
#simdet.read_attrs = ['hdf1', 'cam']
#simdet.hdf1.read_attrs = []  # 'image' gets added dynamically
