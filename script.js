document.addEventListener("DOMContentLoaded", () => {
  const signupBtn = document.getElementById("signup-btn");
  if (signupBtn) {
    signupBtn.onclick = () => {
      window.location.href = "/sign-up";
    };
  }

  const loginBtn = document.getElementById("login-btn");
  if (loginBtn) {
    loginBtn.onclick = () => {
      window.location.href = "/login";
    };
  }

  const addPasswordBtn = document.getElementById("add-password-btn");
  if (addPasswordBtn) {
    addPasswordBtn.onclick = () => {
      window.location.href = "/add-password-page";
    };
  }
});
