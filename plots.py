import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import base64
matplotlib.use('Agg')




df = pd.read_csv('my_data.csv')

numericals = {
    "stone id": "Stone ID",
    "carat": "Carat",
    "base rate": "Base Rate",
    "base off %": "Base Off %",
    "amount": "Amount",
    "rap $/ct": "Rap $/CT",
    "d/r": "D/R",
    "total depth": "Total Depth",
    "table": "Table",
    "girdle%": "Girdle%",
    "c.a": "C.A",
    "p.a": "P.A",
    "c.h": "C.H",
    "p.h": "P.H",
    "lowhalf": "LowHalf",
    "starlenth": "StarLenth",
}

feature_synonyms = {
    "stone id": ["diamond ID", "identification", "unique code", "gem ID", "stone id"],
    "carat": [
        "carat weight",
        "stone weight",
        "diamond weight",
        "gem weight",
        "ct weight",
        "carat",
    ],
    "base rate": [
        "starting price",
        "base cost",
        "reference price",
        "initial price",
        "baseline price",
    ],
    "base off %": [
        "discount rate",
        "percentage off",
        "discount percentage",
        "price reduction",
        "markdown",
    ],
    "amount": [
        "final price",
        "price",
        "total price",
        "total cost",
        "purchase price",
        "selling price",
        "full price",
    ],
    "rap $/ct": [
        "Rappaport Price per Carat",
        "Price per Carat",
        "market value",
        "reference price per carat",
        "industry standard price",
        "Rap price",
    ],
    "d/r": [
        "crown height ratio",
        "crown-to-total height ratio",
        "depth ratio",
        "height proportion",
        "crown-depth ratio",
    ],
    "total depth": [
        "depth percentage",
        "depth proportion",
        "relative depth",
        "depth measure",
        "facet depth",
        "total depth",
    ],
    "table": [
        "table size",
        "table percentage",
        "table facet size",
        "table area",
        "table diameter",
    ],
    "girdle%": [
        "girdle thickness percentage",
        "girdle thickness ratio",
        "girdle size",
        "girdle proportion",
        "girdle measurement",
    ],
    "c.a": [
        "crown angle",
        "upper crown angle",
        "crown facet angle",
        "top angle",
        "main crown angle",
    ],
    "p.a": [
        "pavilion angle",
        "lower pavilion angle",
        "pavilion facet angle",
        "bottom angle",
        "main pavilion angle",
    ],
    "c.h": [
        "crown height",
        "upper half height",
        "crown facet height",
        "top crown height",
    ],
    "p.h": [
        "pavilion height",
        "lower half height",
        "pavilion facet height",
        "bottom pavilion height",
    ],
    "lowhalf": [
        "lower half facet height",
        "underside facet height",
        "culet facet height",
        "pavilion half height",
    ],
    "starlenth": [
        "star facet length",
        "star facet size",
        "culet facet length",
        "bottom facet length",
    ],
}
plot_keywords = {
    "line plot": [
        "vs",
        "compared to",
        "against",
        "compare",
        "comparison of",
        "relationship between",
        "line",
    ],
    "histogram": ["distribution", "spread of", "histogram"],
    "scatter": ["correlation", "scatter"],
    "ratio": ["per"],
    "box plot": ["box plot"],
    "bar chart": ["bar chart", "bar graph"],
}


    
def parseQuery(query):
    features = {}
    relations = {}
    for key in feature_synonyms.keys():
        for word in feature_synonyms[key]:
            if word in query:
                if numericals[key] not in features.keys():
                    idx = query.index(word)
                    features[numericals[key]] = idx
                    break
    for key in plot_keywords.keys():
        for word in plot_keywords[key]:
            if word in query:
                if key not in relations:
                    idx = query.index(word)
                    relations[key] = idx

    return features, relations

def boxplot(features):
  f1 = ''
  for x in features.keys():
    f1 = x

  x = df[f1].values.tolist()
  print(x)
  plt.boxplot(x)
  plt.xlabel(f1)
  plt.title("Box Plot of {}".format(f1))
  plt.savefig("{}_hist.png".format(f1))
  with open("{}_hist.png".format(f1), "rb") as image_file:
      image_data = image_file.read()
  base64_encoded_data = base64.b64encode(image_data).decode('utf-8')
  return base64_encoded_data  


def plotRatio(features):
    f1, f2 = "", ""
    v1, v2 = -1, -1
    for val in features.keys():
        if f1 == "":
            f1 = val
        else:
            f2 = val

    for val in features.values():
        if v1 == -1:
            v1 = val
        else:
            v2 = val

    if v1 < v2:
        nume = f1
        deno = f2
    else:
        nume = f2
        deno = f1
    ratio = df[nume] / df[deno]
    print(ratio)
    print(ratio.values.tolist())
    x = [i for i in range(1, len(ratio) + 1)]
    plt.plot(x, ratio.values.tolist())
    plt.xlabel("different samples")
    plt.ylabel(nume)
    plt.title("{} per {}".format(nume, deno))
    plt.savefig("{}_per_{}.png".format(nume, deno))
    with open("{}_per_{}.png".format(nume, deno), "rb") as image_file:
        image_data = image_file.read()
    base64_encoded_data = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded_data

def plotScatter(features):
    f1, f2 = "", ""
    for val in features.keys():
        if f1 == "":
            f1 = val
        else:
            f2 = val
    x = df[f1].values.tolist()
    y = df[f2].values.tolist()
    plt.scatter(x, y)
    plt.xlabel(f1)
    plt.ylabel(f2)
    plt.title("Scatter plot {} and {}".format(f1, f2))
    plt.savefig("{}_scatter_{}.png".format(f1, f2))
    with open("{}_scatter_{}.png".format(f1, f2), "rb") as image_file:
        image_data = image_file.read()
    base64_encoded_data = base64.b64encode(image_data).decode("utf-8")
    return base64_encoded_data

def lineplot(features):
  f1,f2='',''
  for val in features.keys():
    if f1=='':
      f1 = val
    else:
      f2 = val
  x = df[f1].values.tolist()
  y = df[f2].values.tolist()
  plt.plot(x,y)
  plt.xlabel(f1)
  plt.ylabel(f2)
  plt.title("Line plot of {} and {}".format(f1,f2))
  plt.savefig("{}_line_{}.png".format(f1,f2))
  with open("{}_line_{}.png".format(f1,f2), "rb") as image_file:
      image_data = image_file.read()
  base64_encoded_data = base64.b64encode(image_data).decode('utf-8')
  return base64_encoded_data

def histogram(features):
  f1 = ''
  for x in features.keys():
    f1 = x

  x = df[f1].values.tolist()
  plt.hist(x)
  plt.xlabel(f1)
  plt.title("Distribution of {}".format(f1))
  plt.savefig("{}_hist.png".format(f1))
  with open("{}_hist.png".format(f1), "rb") as image_file:
      image_data = image_file.read()
  base64_encoded_data = base64.b64encode(image_data).decode('utf-8')
  return base64_encoded_data  

def getPlot(features,relations):
    val = ''
    for key in relations.keys():
        val = key
    if len(relations)==0:
        if len(features)==1:
            return histogram(features)
        elif len(features)==2:
            return lineplot(features)
        else:
            return ""
    if val=='line plot':
        if len(features)!=2:
            return ""
        return lineplot(features)
    elif val=='histogram':
        if len(features)!=1:
            return ""
        return histogram(features)
    elif val=='ratio':
        if len(features)!=2:
            return ""
        return plotRatio(features)
    elif val=='box plot':
        if len(features)!=1:
            return ""
        return boxplot(features)
    elif val=='scatter':
        if len(features)!=2:
            return ""
        return plotScatter(features)