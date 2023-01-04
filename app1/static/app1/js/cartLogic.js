console.log('hello');
const increaseBtn = document.querySelectorAll('.increase');
const decreaseBtn = document.querySelectorAll('.decrease');
// const deleteBtn = document.querySelectorAll('.delete');
const cartModalTotal = document.querySelector('.cart-modal-total');
const cartModalTotalMenu = document.querySelector('.cart-modal-total-menu');
const closeBtn = document.querySelector('.close-btn');
const totalAmount = document.querySelector('.total-amount');
const modalContainer = document.querySelector('.modal-container');
const buyBtn = document.querySelector('.buy-btn');
const buyNowBtn = document.querySelectorAll('.buy-now-btn');
const modalMenuContainer = document.querySelector('.modal-container-menu');
const globalInputHidden = document.querySelector('.global-hidden-input');

console.log(buyNowBtn);

buyNowBtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    modalContainer.classList.remove('hidden');
    let individualPrice = e.target.parentElement.children[0].innerText;
    cartModalTotalMenu.innerHTML = individualPrice;
    let inputHidden =
      e.target.parentElement.parentElement.parentElement.children[0];
    globalInputHidden.value = inputHidden.value;
    console.log(globalInputHidden.value);
  });
});

closeBtn.addEventListener('click', () => {
  modalContainer.classList.add('hidden');
  console.log('hello');
});

buyBtn.addEventListener('click', () => {
  modalContainer.classList.remove('hidden');
});

const updateCartTotal = () => {
  let total = 0;
  if (document.getElementsByClassName('cart-container')[0].childNodes) {
    var cartItemContainer =
      document.getElementsByClassName('cart-container')[0];
    console.log(cartItemContainer);
    var cartRows = document.querySelectorAll('.cart-card');
    console.log(cartRows);
    cartRows.forEach((row) => {
      var priceTag = row.querySelector('.price');
      var quantityTag = row.querySelector('.cart-value');
      total =
        total +
        parseFloat(priceTag.innerText) * parseFloat(quantityTag.innerText);
    });
    cartModalTotal.innerHTML = total;
    document.querySelector('.cart-modal-total-hidden').value = total;
  }
  document.querySelector('.total-amount').innerHTML = total;
  document.querySelector('.cart-total-hidden').value = total;
};
window.addEventListener('DOMContentLoaded', updateCartTotal);

increaseBtn.forEach((incBtn) => {
  incBtn.addEventListener('click', (e) => {
    let ele = e.target.parentElement.children[1];
    let currentInput = e.target.parentElement.children[3];
    let value = Number(ele.textContent);
    if (value >= 1) {
      ele.textContent = value += 1;
      console.log('thisis input tag', currentInput);
      currentInput.value = value;

      updateCartTotal();
    } else {
      return;
    }
  });
});

decreaseBtn.forEach((decBtn) => {
  decBtn.addEventListener('click', (e) => {
    let ele = e.target.parentElement.children[1];
    let currentInput = e.target.parentElement.children[3];
    let value = Number(ele.textContent);
    if (value >= 2) {
      ele.textContent = value -= 1;
      currentInput.value = value;
      console.log('this is input', currentInput.value);
      updateCartTotal();
    } else {
      return;
    }
  });
});

// deleteBtn.forEach((btn) => {
//   console.log(btn);
//   btn.addEventListener('click', (e) => {
//     e.currentTarget.parentElement.remove();
//     updateCartTotal();
//   });
// });
