# optical-character-recognition-OCR
<h2>Topic</h2>
this repository aims to convert simple images containing captchas into text.

<h2>Results</h2>
Now the question is how well it performs.It performs pretty good if the given captchas are like the ones the neural network is trained on. that is text on a white background. it fails to recognize some of the characters if the letters look different or if the background is of somewhat different colour. Also note that the dataset on which neural network is trained on does not have some characters like 'L' or '1' etc so it will make wrong predictions on those.Also note that this has been trained on capital letters of english alphabet so it cannot detect small letters from the english alphabet.<br/>
here is an outcome 
<img src="https://github.com/adibyte95/optical-character-recognition-OCR/blob/master/media/output.jpg" /><br/>
some of the errors here are due to absence of letters in the training set like absence of the letter 'O'.others are due to different apperences of training set images which can be fixed due by some data augmentation 

<h2>Note</h2>
please feel free the raise any issue. i am also open to suggestions to improve this project and pull requests


<h2>Credits</h2>
this repository is inspired from a medium post.read more about it <a href ="https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710" target="_blank">here</a>. you can also download the dataset from this post or clone this repository.
