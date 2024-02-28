#Replace It With Your Bucket Name

# To copy all JSON Reference data to same location
aws s3 cp . s3de-on-youtube-raw-useast1-devyoutuberaw_statistics_reference_data --recursive --exclude  --include .json

# To copy all data files to its own location, following Hive-style patterns
aws s3 cp CAvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=ca
aws s3 cp DEvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=de
aws s3 cp FRvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=fr
aws s3 cp GBvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=gb
aws s3 cp INvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=in
aws s3 cp JPvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=jp
aws s3 cp KRvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=kr
aws s3 cp MXvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=mx
aws s3 cp RUvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=ru
aws s3 cp USvideos.csv s3de-on-youtube-raw-useast1-devyoutuberaw_statisticsregion=us

