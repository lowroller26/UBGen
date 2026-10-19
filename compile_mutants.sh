cd mutants
for f in *.c; do
    gcc "$f" -O0 -fsanitize=address -o "../out/${f%.c}.out"
done