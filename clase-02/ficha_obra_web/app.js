const form = document.querySelector('#obra-form');
const resetButton = document.querySelector('#reset-button');
const errorBox = document.querySelector('#form-error');
const emptyResult = document.querySelector('#empty-result');
const obraCard = document.querySelector('#obra-card');

const numberFormat = new Intl.NumberFormat('es-UY', { maximumFractionDigits: 2 });

function definirOrientacion(ancho, alto) {
  if (ancho > alto) return 'horizontal';
  if (alto > ancho) return 'vertical';
  return 'cuadrada';
}

function definirTamanio(area) {
  if (area < 1000) return 'chica';
  if (area <= 5000) return 'mediana';
  return 'grande';
}

function mostrarError(message) {
  errorBox.textContent = message;
  errorBox.hidden = false;
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  errorBox.hidden = true;

  const titulo = document.querySelector('#titulo').value.trim();
  const autor = document.querySelector('#autor').value.trim();
  const anio = Number(document.querySelector('#anio').value);
  const ancho = Number(document.querySelector('#ancho').value);
  const alto = Number(document.querySelector('#alto').value);

  if (!titulo || !autor || !Number.isInteger(anio)) {
    mostrarError('Completá el título, el autor y un año entero.');
    return;
  }
  if (ancho <= 0 || alto <= 0) {
    mostrarError('El ancho y el alto deben ser mayores que cero.');
    return;
  }

  const area = ancho * alto;
  const orientacion = definirOrientacion(ancho, alto);
  const tamanio = definirTamanio(area);

  document.querySelector('#resultado-titulo').textContent = titulo;
  document.querySelector('#resultado-autor').textContent = `${autor} · ${anio}`;
  document.querySelector('#resultado-anio').textContent = anio;
  document.querySelector('#resultado-dimensiones').textContent = `${numberFormat.format(ancho)} × ${numberFormat.format(alto)} cm`;
  document.querySelector('#resultado-area').textContent = `${numberFormat.format(area)} cm²`;
  document.querySelector('#resultado-orientacion').textContent = orientacion;
  document.querySelector('#resultado-tamanio').textContent = tamanio;
  document.querySelector('#preview-orientation').textContent = orientacion.toUpperCase();
  document.querySelector('#art-preview').dataset.orientation = orientacion;

  emptyResult.hidden = true;
  obraCard.hidden = false;
  obraCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
});

resetButton.addEventListener('click', () => {
  errorBox.hidden = true;
  obraCard.hidden = true;
  emptyResult.hidden = false;
  document.querySelector('#titulo').focus();
});
