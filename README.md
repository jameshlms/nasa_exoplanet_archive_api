# NASA Exoplanet Query API
A Python package that streamlines querying from NASA's Exoplanet Archive. The package minimizes requests made to NASA's Exoplanet Archive by caching data in their archive.

## Features
- Ease of use sending requests to and recieving responses from NASA's Exoplanet Archive.
- Caches data from the archive to ensure excessive requests to the archive is avoided.
- Allows for easy querying of the archive but also more advanced querying for more specific requirements.

## Installation
```bash
pip install exopl_archive_api
```
## Usage
```python
import exopl_archive_api as neaa

query_client: neaa.ExoplanetQuery = neaa.ExoplanetQuery()

result = query_service.get_data("SELECT pl_name, pl_orbper FROM ps WHERE st_mass BETWEEN 0.8 AND 1.2")

print(result)
```
## Cache Management
The cache is updated every Sunday at 00:00 (UTC). Cache is updated on a seperate server, ensuring calls to the archive are kept at a minimum.

## Acknoledgements
This package makes use of data from the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration (NASA) under the Exoplanet Exploration Program.

If you use this package in your research or publication, please include the following acknowledgment:

>"This research has made use of the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program."

For specific datasets (e.g., WASP, UKIRT), additional acknowledgments may be required. Please see NASA’s Acknowledgment Guidelines.