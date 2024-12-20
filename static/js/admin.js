document.addEventListener('DOMContentLoaded', function() {
    const categoryField = document.getElementById('id_category');
    const subcategoryField = document.getElementById('id_subcategory');
    const fieldsToHide = {
        'Аксессуары': {
            'Мониторы': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_battery', 'id_ram', 'id_ssd'],
            'Клавиатуры': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_battery', 'id_ram', 'id_ssd'],
            'Мыши': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_battery', 'id_ram', 'id_ssd'],
            'Гарнитура': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_battery', 'id_ram', 'id_ssd'],
        },
    };

function toggleFields() {
    // Получаем выбранные значения
    const selectedCategory = categoryField.options[categoryField.selectedIndex].text.trim();
    const selectedSubcategory = subcategoryField.options[subcategoryField.selectedIndex].text.trim();

    console.log("Выбор категории:", selectedCategory);
    console.log("Выбор подкатегории:", selectedSubcategory);

    // Показываем все поля
    Object.values(fieldsToHide).flat().forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.closest('.form-row').style.display = '';
            console.log(`Показать поле: ${fieldId}`);
        }
    });

    // Скрываем поля в зависимости от выбранной категории и подкатегории
    if (fieldsToHide[selectedCategory] && fieldsToHide[selectedCategory][selectedSubcategory]) {
        const fields = fieldsToHide[selectedCategory][selectedSubcategory];
        fields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (field) {
                console.log(`Скрываем поле: ${fieldId}`);
                field.closest('.form-row').style.display = 'none';
            } else {
                console.log(`Поле не найдено: ${fieldId}`);
            }
        });
    }

    console.log("Состояние полей после скрытия:", selectedCategory, selectedSubcategory);
}



    categoryField.addEventListener('change', toggleFields);
    subcategoryField.addEventListener('change', toggleFields);

    toggleFields();  // Вызовите функцию при загрузке страницы
});

