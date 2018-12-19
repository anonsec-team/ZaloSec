$(document).ready(function () {
  $('#copyright').html('<a href='https://www.zalosec.com/' id='dont_touch'>zalosec</a>');
  setInterval(function () {
      if (!$('#copyright:visible').length) window.location.href = 'https://www.zalosec.com/'
  }, 1000)
})
