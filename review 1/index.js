function applyDiscount(cart, discountCode) {
    let discountAmount = 0;

    if (discountCode === 'SUMMER21') {
        discountAmount = cart.total * 0.1;
    } else if (discountCode === 'WINTER21') {
        discountAmount = cart.total * 0.15;
    } else if (discountCode === 'BLACKFRIDAY') {
        discountAmount = cart.total * 0.25;
    }

    if (discountAmount > 50) {
        discountAmount = 50;
    }

    cart.total -= discountAmount;
    return cart;
}













// solution: 

const DISCOUNT_CODES = {
    'SUMMER21': 0.1,
    'WINTER21': 0.15,
    'BLACKFRIDAY': 0.25,
};

const MAX_DISCOUNT = 50;

function calculateDiscount(cart, discountCode) {
    const discountPercentage = DISCOUNT_CODES[discountCode] || 0;
    let discountAmount = cart.total * discountPercentage;
    return Math.min(discountAmount, MAX_DISCOUNT);
}

function applyDiscount(cart, discountCode) {
    const discountAmount = calculateDiscount(cart, discountCode);
    cart.total -= discountAmount;
    return cart;
}
