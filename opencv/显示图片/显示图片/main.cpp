//#include <opencv2/opencv.hpp>
//#include "opencv2/imgproc/imgproc.hpp"
//#include "opencv2/highgui/highgui.hpp"
//
//int main(int argc,char** argv) {
//
//	//std::string imgFile = "1_d.jpg";
//	cv::Mat img = cv::imread(argv[1],-1);
//	if (img.empty())
//		return -1;
//	cv::namedWindow("Example1", cv::WINDOW_AUTOSIZE);
//	cv::imshow("Example1", img);
//	cv::waitKey(0);
//	cv::destroyWindow("Example1");
//	return 0;
//}

#include <opencv2\opencv.hpp>
int main() {
	std::string filename = "1_d.jpg";
	cv::Mat img = cv::imread(filename,-1);
	if (img.empty())
		return -1;
	cv::namedWindow("Example1", cv::WINDOW_AUTOSIZE);
	cv::imshow("hello", img);
	cv::waitKey(0);
	cv::destroyWindow("Example1");
	return 0;
}