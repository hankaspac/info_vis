import json
import gzip

# Load the gzipped JSON file
with gzip.open('full_nodes_links.json.gz', 'rt', encoding='utf-8') as file:
    data = json.load(file)

# Split nodes and links into chunks
chunk_size = 1000  # Define how many nodes per chunk
chunks = [data['nodes'][i:i + chunk_size] for i in range(0, len(data['nodes']), chunk_size)]

# Split links based on nodes in each chunk
chunked_links = []
for chunk in chunks:
    node_ids = {node['book_id'] for node in chunk}
    chunk_links = [link for link in data['links'] if link['source'] in node_ids and link['target'] in node_ids]
    chunked_links.append(chunk_links)

# Save each chunk to a new gzipped JSON file
for i, (chunk, chunk_links) in enumerate(zip(chunks, chunked_links)):
    chunk_data = {'nodes': chunk, 'links': chunk_links}
    with gzip.open(f'full_nodes_links_chunk_{i}.json.gz', 'wt', encoding='utf-8') as chunk_file:
        json.dump(chunk_data, chunk_file)
