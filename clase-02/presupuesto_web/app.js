const form = document.querySelector('#budget-form');
const anchoInput = document.querySelector('#ancho');
const altoInput = document.querySelector('#alto');
const error = document.querySelector('#error');
const money = new Intl.NumberFormat('es-UY', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const decimal = new Intl.NumberFormat('es-UY', { minimumFractionDigits: 3, maximumFractionDigits: 3 });

function calcularPresupuesto() {
  const ancho = Number(anchoInput.value);
  const alto = Number(altoInput.value);
  error.hidden = true;

  if (!Number.isFinite(ancho) || !Number.isFinite(alto) || ancho <= 0 || alto <= 0) {
    error.textContent = 'Ingresá un ancho y un alto mayores que cero.';
    error.hidden = false;
    return;
  }

  const superficie = (ancho * alto) / 10_000;
  const precioBase = superficie * 450;
  let precioFinal = precioBase;
  let detalle = 'Precio base, sin ajustes.';
  let ajuste = '$0,00';
  let status = 'PRECIO BASE';
  let activeCard = 'normal-card';

  if (superficie > 2) {
    precioFinal = precioBase * 1.15;
    detalle = 'Se aplicó un recargo del 15% por manipulación.';
    ajuste = `+$${money.format(precioFinal - precioBase)}`;
    status = 'RECARGO 15%';
    activeCard = 'surcharge-card';
  } else if (superficie < 0.5) {
    precioFinal = 300;
    detalle = 'Se aplicó el cargo mínimo de $300.';
    ajuste = `+$${money.format(precioFinal - precioBase)}`;
    status = 'CARGO MÍNIMO';
    activeCard = 'minimum-card';
  }

  document.querySelector('#precio-final').textContent = `$${money.format(precioFinal)}`;
  document.querySelector('#precio-base').textContent = `$${money.format(precioBase)}`;
  document.querySelector('#dimensiones').textContent = `${money.format(ancho)} × ${money.format(alto)} cm`;
  document.querySelector('#superficie').textContent = `${decimal.format(superficie)} m²`;
  document.querySelector('#ajuste').textContent = ajuste;
  document.querySelector('#detalle').textContent = detalle;
  document.querySelector('#receipt-status').textContent = status;

  document.querySelectorAll('.conditions article').forEach((card) => card.classList.remove('active'));
  document.querySelector(`#${activeCard}`).classList.add('active');
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  calcularPresupuesto();
});

document.querySelectorAll('[data-width]').forEach((button) => {
  button.addEventListener('click', () => {
    anchoInput.value = button.dataset.width;
    altoInput.value = button.dataset.height;
    calcularPresupuesto();
  });
});
