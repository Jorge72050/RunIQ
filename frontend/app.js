// ============================
// GLOBAL STATE
// ============================
let currentTab = 0;
const tabs = document.getElementsByClassName("tab");
const answers = {};

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  showTab(currentTab);
  attachInputListeners();
  attachButtonListeners();
  attachNavListeners();
});

// ============================
// TAB NAVIGATION
// ============================
function showTab(n) {
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].style.display = "none";
  }

  tabs[n].style.display = "block";

  // Back button
  document.getElementById("prevBtn").style.display =
    n === 0 ? "none" : "inline-block";

  // Next button text
  document.getElementById("nextBtn").innerText =
    n === tabs.length - 1 ? "Submit" : "Next";
}

function nextTab() {
  if (!validateCurrentTab()) return;

  currentTab++;
  if (currentTab >= tabs.length) {
    submitForm();
    return;
  }
  showTab(currentTab);
}

function prevTab() {
  currentTab--;
  showTab(currentTab);
}

// ============================
// NAV BUTTONS
// ============================
function attachNavListeners() {
  document.getElementById("nextBtn").addEventListener("click", nextTab);
  document.getElementById("prevBtn").addEventListener("click", prevTab);
}

// ============================
// INPUT HANDLING
// ============================
function attachInputListeners() {
  document.querySelectorAll("input, select").forEach(el => {
    el.addEventListener("input", () => {
      saveValue(el);
      el.classList.remove("invalid");
    });

    el.addEventListener("change", () => {
      saveValue(el);
      el.classList.remove("invalid");
    });
  });
}

function saveValue(el) {
  const key = el.id || el.name;
  if (!key) return;
  answers[key] = el.value;
}

// ============================
// OPTION BUTTONS
// ============================
function attachButtonListeners() {
  document.querySelectorAll(".option").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();

      const value = btn.innerText.trim();
      const key = btn.dataset.key || `tab_${currentTab}`;

      answers[key] = value;

      // Highlight selection
      const buttons = tabs[currentTab].querySelectorAll(".option");
      buttons.forEach(b => b.classList.remove("selected"));
      btn.classList.add("selected");
    });
  });
}

// ============================
// VALIDATION
// ============================
function validateCurrentTab() {
  const tab = tabs[currentTab];

  // 1️⃣ If this tab has option buttons, require one selected
  const optionButtons = tab.querySelectorAll(".option");
  if (optionButtons.length > 0) {
    const selected = tab.querySelector(".option.selected");
    if (!selected) {
      alert("Please select an option before continuing.");
      return false;
    }
    return true;
  }

  // 2️⃣ Otherwise validate inputs/selects
  const inputs = tab.querySelectorAll("input, select");
  for (let el of inputs) {
    if (el.value.trim() === "") {
      el.classList.add("invalid");
      return false;
    }
  }

  return true;
}

// ============================
// SUBMIT
// ============================
function submitForm() {
  console.log("FINAL ANSWERS:", answers);

  // Example POST to Flask
  /*
  fetch("/onboarding", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(answers)
  });
  */

  alert("Form submitted! Check console for data.");
}
