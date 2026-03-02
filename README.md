const loadMoreModels = (() => {
  if (catalog.value?.meta.current_page && catalog.value?.meta.last_page > catalog.value?.meta.current_page) {
    el.value = document.querySelector('#catalog-item:last-of-type');
    position.value = el.value.getBoundingClientRect()
    isVisible.value = useElementVisibility(el.value)
    console.log(isVisible.value)
    console.log(el.value)
    console.log(position.value)
    console.log(`Позиция: bottom ${position.value.bottom}, y ${position.value.y} , x ${position.value.x}, top ${position.value.top},height ${position.value.height} `);
    if (catalog.value?.meta.current_page === 1 ) {
      setPage(catalog.value?.meta.current_page + 1)
      isLoaded.value = false
    }else if (catalog.value?.meta.current_page !== 1 && isVisible.value === true) {
      setPage(catalog.value?.meta.current_page + 1)
      isLoaded.value = false
    }
  }
})
