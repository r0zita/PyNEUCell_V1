with open("xxendcaps.mdl") as f:
    data = f.read()

# Extract and count vertex lines
verts = data.split("VERTEX_LIST")[1].split("}")[0]
v_lines = [line for line in verts.splitlines() if "[" in line]
num_vertices = len(v_lines)

# Extract and validate element connections
elements = data.split("ELEMENT_CONNECTIONS")[1].split("}")[0]
e_lines = [line for line in elements.splitlines() if "[" in line]

bad_elements = []
for line in e_lines:
    cleaned = line.strip("[], \t\n")
    try:
        indices = [int(i.strip()) for i in cleaned.split(",")]
        if any(i >= num_vertices for i in indices):
            bad_elements.append(line)
    except ValueError as e:
        print(f"[ERROR] Could not parse line: {line.strip()} ({e})")

print(f"Total vertices: {num_vertices}")
print(f"Total element connections: {len(e_lines)}")
print(f"Bad elements with out-of-bounds indices: {len(bad_elements)}")
if bad_elements:
    print("Example bad elements:")
    for be in bad_elements[:5]:
        print("   ", be.strip())

