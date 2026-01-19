function expandAllDescendants(parentLevel) {
    const children = document.querySelectorAll('tr[data-parent="' + parentLevel + '"]');
    children.forEach(function(row) {
        row.style.display = '';
        if (row.classList.contains('parent-row')) {
            const childIcon = row.querySelector('.toggle-icon');
            if (childIcon) childIcon.textContent = '▾';
            const childLevel = row.getAttribute('data-level');
            expandAllDescendants(childLevel);
        }
    });
}

function collapseAllDescendants(parentLevel) {
    const children = document.querySelectorAll('tr[data-parent="' + parentLevel + '"]');
    children.forEach(function(row) {
        row.style.display = 'none';
        if (row.classList.contains('parent-row')) {
            const childIcon = row.querySelector('.toggle-icon');
            if (childIcon) childIcon.textContent = '▸';
            const childLevel = row.getAttribute('data-level');
            collapseAllDescendants(childLevel);
        }
    });
}

function toggleChildren(parentRow) {
    const level = parentRow.getAttribute('data-level');
    const icon = parentRow.querySelector('.toggle-icon');
    const isCollapsed = icon.textContent === '▸';

    icon.textContent = isCollapsed ? '▾' : '▸';

    if (isCollapsed) {
        expandAllDescendants(level);
    } else {
        collapseAllDescendants(level);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("tr.parent-row").forEach(row => {
        row.addEventListener("click", () => toggleChildren(row));
    });
});
