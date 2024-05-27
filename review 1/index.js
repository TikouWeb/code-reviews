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
