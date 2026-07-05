// Auto-dismiss alerts after 5s
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      alert.style.transition = 'opacity .4s ease, transform .4s ease';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(100%)';
      setTimeout(() => alert.remove(), 400);
    }, 5000);
  });

  // Quantity input: submit form on manual change after brief delay
  document.querySelectorAll('.cart-row input[type="number"]').forEach(input => {
    let timer;
    input.addEventListener('input', () => {
      clearTimeout(timer);
      timer = setTimeout(() => input.closest('form').submit(), 800);
    });
  });
});
