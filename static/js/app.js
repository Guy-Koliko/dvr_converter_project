// UI Variables
const UIvideosPlaylist = document.querySelector('.right-videos-container1');
const UIvideoSubTitle = document.querySelector(
  '.left-container1 .video-subtitle'
);
const UIvideoTitle = document.querySelector('.left-container1 .video-title');
const UIiframePlayer = document.querySelector('.left-container1 .iframe-player');

// Events
UIvideosPlaylist.addEventListener('click', getVideoData);

// Get the video data from the item clicked
function getVideoData(e) {
  if (e.target.classList.contains('video')) {
    const iframe = e.target.firstElementChild;
    const videoUrl = iframe.getAttribute('src');
    const videoTitle = iframe.nextElementSibling.firstElementChild.textContent;

    const videoInfo = {
      videoUrl,
      videoTitle,
    };

    prepareFrame(videoInfo);
  }
}

// Prepare the video
function prepareFrame(videoInfo) {
  const { videoUrl, videoTitle, videoSubTitle } = videoInfo;

  // Update frame
  UIvideoTitle.textContent = videoTitle;
  UIvideoSubTitle.textContent = videoSubTitle;
  UIiframePlayer.setAttribute('src', videoUrl);
  var ifrm = document.createElement('video');
}
