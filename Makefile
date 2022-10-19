server:
	sleep 1 && open http://localhost:8000 &
	cd public && python3 ../server.py
