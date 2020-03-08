build:
	cd backend && npm install \
	cd frontend && npm install \
	cd frontend && npm run-script build

clean:
	rm -rfv ./frontend/node_modules \
	rm -rfv ./backend/node_modules \
	rm -rfv ./frontend/package-lock.json \
	rm -rfv ./backend/package-lock.json

run:
	npm start --prefix backend