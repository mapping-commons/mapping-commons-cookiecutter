# OLS Mapping Commons
Experimental SSSOM repo for all OLS based ontologies and their mappings

To update the mapping registry from OLS:

```sh
sh odk.sh make update_registry -B
```

To update the mappings:

```sh
sh odk.sh make mappings
```

If the run requires a recently published SSSOM or OAK feature, first update ODK:

```sh
docker pull obolibrary/odkfull:dev
```

and then run the `dependencies` goal together with the mappings goal:


```sh
IMAGE=odkfull:dev sh odk.sh make mappings
```

*Note: If running on a Windows machine, replace `sh odk.sh` with `odk.bat` in the above commands.*

## Design decisions:

1. Only mappings of base entities are extracted. This ensures that we do not import the same UBERON mapping for every species specific anatomy ontology (XAO). This is realised as a filtering step that relies on the crude assumption that the ontology ID is somehow reflected in the subject_id.
