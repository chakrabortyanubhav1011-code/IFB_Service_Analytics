INSERT INTO dim_branch (branch_name)
SELECT DISTINCT branch_name
FROM pending_calls;

INSERT INTO dim_franchise (franchise_name)
SELECT DISTINCT franchise_name
FROM pending_calls;

INSERT INTO dim_product (product, model)
SELECT DISTINCT product, model
FROM pending_calls;

INSERT INTO dim_technician (technician_name)
SELECT DISTINCT technician_name
FROM pending_calls;
