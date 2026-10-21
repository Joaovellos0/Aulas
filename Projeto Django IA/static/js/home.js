/**
 * MÙSIC Shop - JavaScript Home (Vitrine em Carrossel Estilo Ibanez Dinâmico)
 * Controle de Filtro por Marcas e Paginação de 3 Produtos por Bloco SEM LIMITES de Páginas.
 * Transições Fluidas nos cards ao navegar e trocar de marca.
 */

document.addEventListener('DOMContentLoaded', function () {
    initVitrineShowcase();
});

function initVitrineShowcase() {
    const filterBtns = document.querySelectorAll('.vitrine_filter_btn');
    const brandBlocks = document.querySelectorAll('.vitrine_brand_block');
    const paginationContainer = document.getElementById('vitrine_pagination');
    const arrowPrev = document.getElementById('vitrine_arrow_prev');
    const arrowNext = document.getElementById('vitrine_arrow_next');

    if (!filterBtns.length || !brandBlocks.length || !paginationContainer) return;

    let currentMarcaId = null;
    let currentPage = 1;
    let totalPages = 1;

    // Escuta cliques nas setas das extremidades
    if (arrowPrev) {
        arrowPrev.addEventListener('click', () => {
            if (currentPage > 1) {
                goToPage(currentPage - 1);
            }
        });
    }

    if (arrowNext) {
        arrowNext.addEventListener('click', () => {
            if (currentPage < totalPages) {
                goToPage(currentPage + 1);
            }
        });
    }

    // 1. Alternância de Marca pelo Filtro
    filterBtns.forEach((btn) => {
        btn.addEventListener('click', function () {
            if (this.classList.contains('active')) return;

            // Atualiza botões do filtro com animação fluida
            filterBtns.forEach((b) => b.classList.remove('active'));
            this.classList.add('active');

            const marcaId = this.dataset.marcaId;
            selectMarca(marcaId);
        });
    });

    function selectMarca(marcaId) {
        currentMarcaId = marcaId;
        currentPage = 1;

        // Ativa o bloco da marca selecionada e calcula dinamicamente as páginas
        brandBlocks.forEach((block) => {
            if (block.dataset.marcaId === marcaId) {
                block.classList.add('active');
                
                // Calcula dinamicamente quantas páginas existem neste bloco (sem travas ou limites fixos)
                const pages = block.querySelectorAll('.vitrine_page');
                totalPages = pages.length;
                block.dataset.totalPages = totalPages;
                
                showPage(block, 1);
            } else {
                block.classList.remove('active');
            }
        });

        // Atualiza estado das setas de borda e indicadores de página
        updateEdgeArrows();
        renderIndicators();
    }

    function showPage(block, pageNum) {
        const pages = block.querySelectorAll('.vitrine_page');
        pages.forEach((page) => {
            const p = parseInt(page.dataset.page, 10);
            if (p === pageNum) {
                // Remove e readiciona a classe 'active' com reflow para re-disparar a animação fluida dos cards
                page.classList.remove('active');
                void page.offsetWidth; // Dispara reflow para reiniciar animação CSS dos cards
                page.classList.add('active');
            } else {
                page.classList.remove('active');
            }
        });
    }

    function updateEdgeArrows() {
        if (!arrowPrev || !arrowNext) return;

        if (totalPages <= 1) {
            arrowPrev.style.display = 'none';
            arrowNext.style.display = 'none';
        } else {
            arrowPrev.style.display = 'inline-flex';
            arrowNext.style.display = 'inline-flex';
            arrowPrev.disabled = currentPage === 1;
            arrowNext.disabled = currentPage === totalPages;
        }
    }

    // 2. Renderização dos Indicadores de Página (Estilo dos filtros de marca, tamanho compacto)
    function renderIndicators() {
        paginationContainer.innerHTML = '';

        // Se tiver apenas 1 página ou menos, não há necessidade de indicadores
        if (totalPages <= 1) {
            return;
        }

        // Botões Numéricos servindo exclusivamente como indicadores visuais da página atual
        for (let i = 1; i <= totalPages; i++) {
            const indicator = document.createElement('button');
            indicator.className = `vitrine_page_indicator ${i === currentPage ? 'active' : ''}`;
            indicator.textContent = i;
            indicator.dataset.page = i;
            indicator.type = 'button';
            indicator.title = `Página ${i} de ${totalPages}`;
            indicator.setAttribute('aria-label', `Página ${i} de ${totalPages}`);
            // Permite também alternar para a página ao clicar no indicador para máxima flexibilidade
            indicator.addEventListener('click', () => {
                goToPage(i);
            });
            paginationContainer.appendChild(indicator);
        }
    }

    function goToPage(pageNum) {
        if (pageNum < 1 || pageNum > totalPages) return;
        currentPage = pageNum;
        
        const activeBlock = document.querySelector(`.vitrine_brand_block[data-marca-id="${currentMarcaId}"]`);
        if (activeBlock) {
            showPage(activeBlock, pageNum);
        }
        updateEdgeArrows();
        renderIndicators();
    }

    // Inicialização com a primeira marca ativa
    const initialActiveBtn = document.querySelector('.vitrine_filter_btn.active') || filterBtns[0];
    if (initialActiveBtn) {
        initialActiveBtn.classList.add('active');
        selectMarca(initialActiveBtn.dataset.marcaId);
    }
}
