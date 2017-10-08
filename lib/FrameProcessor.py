import requests
from pprint import pprint
from vision.VisionDriver import getLabelsFromFrame

def remove_cruft(s):
	return s[6:]

def ProcessFrames(frame_list, video_id):
	filenames = [remove_cruft(s) for s in frame_list]
	
	for frame_file in filenames:
		#FIRST Call vision and get Labels
		label_list = getLabelsFromFrame(frame_file)

		splitted_name = frame_file.split("_")
		frame_url = "http://127.0.0.1:8000/deepseek/frame/"+splitted_name[1]+"/media/"+frame_file+"/video/"+splitted_name[0]+"/add/"
		r = requests.post(frame_url)

		for label in label_list:
			label_url="http://127.0.0.1:8000/deepseek/ann/"+label.description+"/frame/"+r.text+"/add/"
			s = requests.post(label_url)
			print "INFO: %s => %s " %(label.description,r.text)

	video_finish_url = "http://127.0.0.1:8000/deepseek/video/"+str(video_id)+"/finish/"
	t = requests.post(video_finish_url)
	print "INFO: Completed processing Video %s " %(str(video_id))


if __name__ == "__main__":
	frame_list = ['media/22_49_72.jpg', 'media/22_52_75.jpg', 'media/22_33_20.jpg', 'media/22_33_15.jpg', 'media/22_49_71.jpg', 'media/22_33_18.jpg', 'media/22_38_47.jpg', 'media/22_43_58.jpg', 'media/22_52_74.jpg', 'media/22_43_57.jpg', 'media/22_32_16.jpg', 'media/22_33_17.jpg', 'media/22_26_9.jpg', 'media/22_35_31.jpg', 'media/22_19_6.jpg', 'media/22_34_23.jpg', 'media/22_80_92.jpg', 'media/22_52_77.jpg', 'media/22_35_25.jpg', 'media/22_45_62.jpg', 'media/22_73_89.jpg', 'media/22_43_56.jpg', 'media/22_43_60.jpg', 'media/22_48_69.jpg', 'media/22_69_87.jpg', 'media/22_52_78.jpg', 'media/22_36_35.jpg', 'media/22_8_2.jpg', 'media/22_41_51.jpg', 'media/22_37_43.jpg', 'media/22_47_66.jpg', 'media/22_40_50.jpg', 'media/22_33_19.jpg', 'media/22_43_53.jpg', 'media/22_35_30.jpg', 'media/22_47_64.jpg', 'media/22_21_10.jpg', 'media/22_37_44.jpg', 'media/22_42_52.jpg', 'media/22_36_33.jpg', 'media/22_35_29.jpg', 'media/22_21_8.jpg', 'media/22_58_84.jpg', 'media/22_37_42.jpg', 'media/22_76_91.jpg', 'media/22_30_11.jpg', 'media/22_65_86.jpg', 'media/22_37_45.jpg', 'media/22_75_90.jpg', 'media/22_72_88.jpg', 'media/22_54_82.jpg', 'media/22_52_76.jpg', 'media/22_43_54.jpg', 'media/22_36_36.jpg', 'media/22_57_83.jpg', 'media/22_36_34.jpg', 'media/22_53_80.jpg', 'media/22_48_70.jpg', 'media/22_33_21.jpg', 'media/22_36_38.jpg', 'media/22_36_32.jpg', 'media/22_30_12.jpg', 'media/22_20_7.jpg', 'media/22_9_3.jpg', 'media/22_43_55.jpg', 'media/22_35_26.jpg', 'media/22_54_85.jpg', 'media/22_37_39.jpg', 'media/22_43_59.jpg', 'media/22_11_5.jpg', 'media/22_53_81.jpg', 'media/22_4_1.jpg', 'media/22_38_48.jpg', 'media/22_47_68.jpg', 'media/22_39_49.jpg', 'media/22_32_13.jpg', 'media/22_43_61.jpg', 'media/22_35_28.jpg', 'media/22_34_24.jpg', 'media/22_35_27.jpg', 'media/22_36_37.jpg', 'media/22_37_46.jpg', 'media/22_34_22.jpg', 'media/22_32_14.jpg', 'media/22_37_40.jpg', 'media/22_47_65.jpg', 'media/22_47_67.jpg', 'media/22_46_63.jpg', 'media/22_52_79.jpg', 'media/22_50_73.jpg', 'media/22_10_4.jpg', 'media/22_37_41.jpg']
	ProcessFrames(frame_list,22)
