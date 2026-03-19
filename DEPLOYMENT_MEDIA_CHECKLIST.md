# Deployment Media Checklist (Heroku + Cloudinary)

## Current audit snapshot (local)
- Total products: 49
- Products with ImageField value: 31
- Products with image_url value: 49
- Products missing both image sources: 0
- ImageField files present in local media: 31/31

## Recommended storage split
- Keep UI/design assets in static/ (logos, icons, placeholders, CSS/JS images).
- Keep Product.image files in media storage (uploaded content).
- Keep fallback placeholder in static/ (already using static/images/noimage-starfleet.svg).

## Heroku config vars (required)
Set these in Heroku app settings:
- SECRET_KEY
- CLOUDINARY_URL
- DATABASE_URL
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET

## Django settings checks
- SECRET_KEY must be loaded from environment in production.
- DEBUG must be False in production.
- ALLOWED_HOSTS must include your Heroku domain.
- Cloudinary media backend should be enabled when CLOUDINARY_URL exists.

## Data and media flow before deploy
1. Confirm every product has either Product.image or image_url.
2. Prefer Product.image for your own product assets.
3. For products currently relying on image_url, verify external links are stable.
4. In production admin, upload/replace images to populate Product.image where needed.

## Deployment verification after release
1. Open products list page and verify images load over HTTPS.
2. Open at least 3 product detail pages with uploaded images.
3. Check one product without Product.image and confirm themed static fallback appears.
4. Add item to bag and verify fallback image appears in bag/checkout/toast if needed.
5. Confirm no requests to /media/noimage.png remain.

## Optional hardening
- Add a management command to report products missing Product.image.
- Add a smoke test for product image rendering in templates.
- Remove any unused local media files after Cloudinary migration is complete.
