-- Write a SQL script that lists all bands with Glam rock as their main
-- style, ranked by their longevity
-- The expression IFNULL(split, 2020) - IFNULL(formed, 0) is used to ensure
-- that if the "split" column is null, it's treated as if it contains the
-- value 2020, and if the "formed" column is null, it's treated as if it
-- contains the value 0. This ensures we do not have a null value for lifespan
-- calculation.


SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0)
AS lifespan FROM metal_bands WHERE style like '%Glam rock%'
ORDER BY lifespan DESC;
