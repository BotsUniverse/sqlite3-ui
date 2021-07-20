function startLoader() {
  if (document.body.classList.contains('loading')) {
    return false;
  }
  else{
    document.body.classList.add('loading');
    return true;
  }
}

function endLoader() {
  if (!document.body.classList.contains('loading')) {
    return false;
  }
  else{
    document.body.classList.add('loading');
    return true;
  }
}

function editTemp() {
  
}