# weibo_user_followers
Process the information of the followers of Weibo users.
## main code
`get_follower_info.py`<br>
 Use regular matching to match all the information of all followers of weibo users.<br>
 `data_deduplication.py`<br>
 Reprocessing the stored data of the followers. <br>
 ## Operating environment
Based on python2.7, first need to install：<br>
1.re <br>
2.os
## Sample
* run **get_follower_info.py**
> First, according to the weibo user data in the **data** directory, all the information of all the people concerned by the user is matched.<br>
> Second, store the matched data in the **follower** directory.<br>
* run **data_deduplication.py**
> Then, take the data from the **follower** directory and *perform deduplication*.<br>
> Finally, save the reprocessed data in the **de_follower** directory.<br>
* The data storage format is as follows:<br>
<img src="https://github.com/C-YC/weibo_user_followers/blob/master/photo/data_format.png" width="400" height="300"/>

* labels

|id|star|star_nickname|star_info|star_way|star_area|star_type|star_gender|star_follow_num|star_fan_num|star_weibo_num|star_level|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
