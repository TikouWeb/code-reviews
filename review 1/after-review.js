const DISCOUNT_MAPPING = {
    'SUMMER21': 0.1,
    'WINTER21': 0.15,
    'BLACKFRIDAY': 0.25,
    default: 0
}

const DISCOUNT_MAX = 50

function applyDiscount(cart) {
    const discountAmount = calculateDiscount(discountCode)
    const newTotal = { ...cart }
    // avoid mutating variables
    newTotal.total -= discountAmount;
    return newTotal;
}

function calculateDiscount(discountCode = "default") {
    let discountAmount = 0;

    const discountRate = DISCOUNT_MAPPING[discountCode] ?? 0
    discountAmount = cart.total * discountRate

    // maximum amount must be 50
    return Math.min(discountAmount, DISCOUNT_MAX)
}