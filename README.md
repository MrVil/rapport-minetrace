# Rapport Minetrace
Par [Bastien Guyl](http://bastien.guyl.me) et [Marc Zominy](https://github.com/zominym)

### Sommaire
* [Présentation du projet](#markdown-header-présentation-du-projet)
* [Transformation des données](#markdown-header-transformation-des-données)
* [Mise en place de la structure dans kTBS](#markdown-header-mise-en-place-de-la-structure-dans-ktbs)
* [Mise en place des transformations](#markdown-header-mise-en-place-des-transformations)
* [Visualisation des données](#markdown-header-visualisation-des-données)
* [Analyse des données](#markdown-header-analyse-des-données)
* [Conclusion](#markdown-header-conclusion)

### Présentation du projet <a name="markdown-header-présentation-du-projet"></a>
Ceci est le rapport d'un [projet](http://liris.cnrs.fr/~pchampin/2016/m2ia-knodyn/project.html) de cours de *Dynamique des connaissances* en Master 2 en Intelligence Artificielle de l'Université Claude Bernard Lyon 1.

Le but est d'étudier des données provenant du jeu [Minecraft](http://minecraft.net) générées par le plugin [Minetrace](https://github.com/Lyon1-Asterix/Minetrace).
Nous traitons ensuite les données avec le script NodeJs **transform.js** disponible ci-joint et nous les insérons dans la plateforme [kTBS](https://liris-ktbs01.insa-lyon.fr:8000/public/) de l'université.

Notre base se situe à l'adresse suivante : [liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/zguyl/](https://liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/zguyl/)

### Mise en place de la structure dans kTBS <a name="markdown-header-mise-en-place-de-la-structure-dans-ktbs"></a>
Les données mises à notre disposition sont propice à être hierarchisées. Cependant, étant donné leur faible diversité, cela nous a conduit à établir une structure plate, plus facile et rapide à utiliser.
Cependant, un exemple de structure hierarchisée est disponible [ici](https://github.com/MrVil/OWL-Minetrace)
Etant donné qu'on ne souhaite pas s'intéresser aux craft, on ne récupère que les informations de base de cette action.

Voici le schéma de la structure produite :
![structure](structure.png)

Et les requêtes envoyées au serveur kTBS :
##### Création de la base
`POST:https://liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/`
```json
{
    "@id": "zguyl/",
    "@type": "Base"
}
```

##### Création du model
`POST:https://liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/zguyl/`
```json
{
    "@id": "model1",
    "@type": "TraceModel"
}
```
`PUT:https://liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/zguyl/model1`
```json
`{
            "@id": "#PlayerKick" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#PlayerDamage" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#PickupItem" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#DropItem" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#PlayerDeath" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#BlockBreak" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#PlayerQuit" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#Craft" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#BlockPlace" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#PlayerJoin" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#Mining" ,
            "@type": "ObselType" 
        },
        {
            "@id": "#x" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerKick", "#PlayerDamage", "#PickupItem", "#DropItem", "#PlayerDeath", "#BlockBreak", "#PlayerQuit", "#Craft", "#BlockPlace", "#PlayerJoin", "#Mining"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "x"
        },
        {
            "@id": "#z" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerKick", "#PlayerDamage", "#PickupItem", "#DropItem", "#PlayerDeath", "#BlockBreak", "#PlayerQuit", "#Craft", "#BlockPlace", "#PlayerJoin", "#Mining"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "z"
        },
        {
            "@id": "#y" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerKick", "#PlayerDamage", "#PickupItem", "#DropItem", "#PlayerDeath", "#BlockBreak", "#PlayerQuit", "#Craft", "#BlockPlace", "#PlayerJoin", "#Mining"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "y"
        },
        {
            "@id": "#playerName" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerKick", "#PlayerDamage", "#PickupItem", "#DropItem", "#PlayerDeath", "#BlockBreak", "#PlayerQuit", "#Craft", "#BlockPlace", "#PlayerJoin", "#Mining"] ,
            "hasAttributeDatatype": ["xsd:string"] ,
            "label": "Player name"
        },
        {
            "@id": "#data" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PickupItem", "#DropItem", "#BlockBreak", "#BlockPlace"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "data"
        },
        {
            "@id": "#blockName" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#BlockBreak", "#BlockPlace"] ,
            "hasAttributeDatatype": ["xsd:string"] ,
            "label": "Block name"
        },
        {
            "@id": "#itemName" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PickupItem", "#DropItem", "#Mining"] ,
            "hasAttributeDatatype": ["xsd:string"] ,
            "label": "Item name"
        },
        {
            "@id": "#amount" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PickupItem", "#DropItem"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "Amount"
        },
        {
            "@id": "#damage" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerDamage"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "damage"
        },
        {
            "@id": "#cause" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#PlayerDamage"] ,
            "hasAttributeDatatype": ["xsd:string"] ,
            "label": "cause"
        },
        {
            "@id": "#resultBCraft" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#Craft"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "Result B Craft"
        },
        {
            "@id": "#numberOfCrafts" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#Craft"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "Number of craft"
        },
        {
            "@id": "#resultData" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#Craft"] ,
            "hasAttributeDatatype": ["xsd:integer"] ,
            "label": "Result data"
        },
        {
            "@id": "#resultType" ,
            "@type": "AttributeType" ,
            "hasAttributeObselType": ["#Craft"] ,
            "hasAttributeDatatype": ["xsd:string"] ,
            "label": "Result type"
        } ]
```

##### Création de la trace
`POST:https://liris-ktbs01.insa-lyon.fr:8000/public/master-ia-2016/zguyl/`
```json
{
    "@id": "t01/",
    "@type": "StoredTrace",
    "hasModel": "model1/"
}
```

### Transformation des données <a name="markdown-header-transformation-des-données"></a>
Pour la transformation des données, deux versions du script

### Mise en place des transformations <a name="markdown-header-mise-en-place-des-transformations"></a>
TODO

### Visualisation des données <a name="markdown-header-visualisation-des-données"></a>
TODO

### Analyse des données <a name="markdown-header-analyse-des-données"></a>
TODO

### Conclusion <a name="markdown-header-conclusion"></a>
TODO
