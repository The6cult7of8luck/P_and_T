import pytest
from order import calculate_total

# === ТЕСТЫ ИЗ ЗАДАНИЯ ===

def test_no_discount():
    """Позитивный: расчёт без скидки."""
    assert calculate_total([{"price": 100, "qty": 2}]) == 200.00

def test_discount_50():
    """Позитивный: скидка 50%."""
    assert calculate_total([{"price": 100, "qty": 2}], 50) == 100.00

def test_invalid_discount():
    """Негативный: скидка больше 100%."""
    with pytest.raises(ValueError):
        calculate_total([{"price": 100, "qty": 1}], 101)

def test_promo_caps_discount_at_100():
    """Интеграционный: промокод и скидка 95% — итоговая скидка не более 100%."""
    assert calculate_total([{"price": 100, "qty": 1}], 95, "SALE10") == 0.00


# === ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ  ===

def test_unknown_promo():
    """Позитивный: неизвестный промокод должен игнорироваться."""
    assert calculate_total([{"price": 50, "qty": 2}], 10, "UNKNOWN") == 90.00

def test_boundary_discount_100():
    """Граничный: скидка ровно 100% без промокода."""
    assert calculate_total([{"price": 100, "qty": 5}], 100) == 0.00