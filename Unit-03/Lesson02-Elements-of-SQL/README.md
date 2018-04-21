# Tables in the `zoo` Database

## animals
This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.
* name — the animal's name (example: 'George')       
* species — the animal's species (example: 'gorilla')       
* birthdate — the animal's date of birth (example: '1998-05-18')       

## diet
This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one. If a species eats more than one food, there will be more than one row for that species.

* species — the name of a species (example: 'hyena')       
* food — the name of a food that species eats (example: 'meat')

## taxonomy
This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.

* name — the common name of the species (e.g. 'jackal')
* species — the taxonomic species name (e.g. 'aureus')
* genus — the taxonomic genus name (e.g. 'Canis')
* family — the taxonomic family name (e.g. 'Canidae')
* t_order — the taxonomic order name (e.g. 'Carnivora')

## ordernames
This table gives the common names for each of the taxonomic orders in the taxonomy table.
* t_order — the taxonomic order name (e.g. 'Cetacea')
* name — the common name (e.g. 'whales and dolphins')


# The SQL for it
```sql
create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);
```
