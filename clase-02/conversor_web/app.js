const form = document.querySelector('#converter-form');
const input = document.querySelector('#centimetros');
const error = document.querySelector('#error');
const pulgadasOutput = document.querySelector('#pulgadas');
const milimetrosOutput = document.querySelector('#milimetros');
const status = document.querySelector('#status');
const statusSymbol = document.querySelector('#status-symbol');
const statusTitle = document.querySelector('#status-title');
const statusText = document.querySelector('#status-text');
const measureBar = document.querySelector('#measure-bar');
const comparisonCopy = document.querySelector('#comparison-copy');

const formatter = new Intl.NumberFormat('es-UY', {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

function convertir() {
  const centimetros = Number(input.value);
  error.hidden = true;

  if (!Number.isFinite(centimetros) || centimetros <= 0) {
    error.textContent = 'Ingresá una medida mayor que cero.';
    error.hidden = false;
    return;
  }

  const pulgadas = centimetros / 2.54;
  const milimetros = centimetros * 10;
  const entra = centimetros <= 30;

  pulgadasOutput.textContent = formatter.format(pulgadas);
  milimetrosOutput.textContent = formatter.format(milimetros);
  status.className = `status ${entra ? 'success' : 'fail'}`;
  statusSymbol.textContent = entra ? '✓' : '×';
  statusTitle.textContent = entra ? 'ENTRA EN EL MARCO' : 'NO ENTRA EN EL MARCO';
  statusText.textContent = entra
    ? `${formatter.format(centimetros)} cm está dentro del límite de 30 cm.`
    : `${formatter.format(centimetros)} cm supera el límite por ${formatter.format(centimetros - 30)} cm.`;

  measureBar.style.width = `${Math.min((centimetros / 30) * 100, 100)}%`;
  comparisonCopy.textContent = entra
    ? `La medida ocupa ${Math.round((centimetros / 30) * 100)}% del marco.`
    : `La medida equivale al ${Math.round((centimetros / 30) * 100)}% del marco y lo supera.`;
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  convertir();
});

document.querySelectorAll('[data-value]').forEach((button) => {
  button.addEventListener('click', () => {
    input.value = button.dataset.value;
    convertir();
  });
});
