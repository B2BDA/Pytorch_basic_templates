import torch
import torch.nn as nn


class TabularModel(nn.Module):
    
    def __init__(self, embed_size, n_cont, n_out, neuron_layer, prob = 0.5):
        super().__init__()
        self.embed = nn.ModuleList([nn.Embedding(ni,nf) for ni,nf in embed_size])
        self.embed_drop = nn.Dropout(prob)
        self.batchnorm_cont = nn.BatchNorm1d(n_cont)
        
        num_embed = sum([nf for ni,nf in embed_size])
        n_input = num_embed + n_cont
        
        layerlist = []
        for i in neuron_layer:
            layerlist.append(nn.Linear(n_input,i))
            layerlist.append(nn.ReLU(inplace=True))
            layerlist.append(nn.BatchNorm1d(i))
            layerlist.append(nn.Dropout(prob))
            n_input = i
        layerlist.append(nn.Linear(neuron_layer[-1], n_out))
        self.layers = nn.Sequential(*layerlist)
        
    def forward(self, x_cat, x_cont):
        embeddings = []
        for i,e in enumerate(self.embed):
            embeddings.append(e(x_cat[:,i]))
        x = torch.cat(embeddings, axis = 1)
        x = self.embed_drop(x)
        x_cont = self.batchnorm_cont(x_cont)
        x = torch.cat([x,x_cont], axis =1)
        x = self.layers(x)
        return x
    
# date = '2010-04-19 08:17:56 UTC'
# fare_class = 0
# passenger_count = 1
# plong = -73.992365
# plat = 40.730521
# dlong = -73.975499
# dlat = 40.744746

# data = DataProcess()
# x_cat, x_cont = data.process(date, plat, plong, dlat, dlong, fare_class, passenger_count)
# embed_size = [(24, 12), (2, 1), (7, 4)]
# model_l = TabularModel(embed_size,3,1,[32,64,128])
# model_l.load_state_dict(torch.load('taxiModelRegression.pt'))
# model_l.eval()
# with torch.no_grad():
#     y = model_l(x_cat, x_cont)
#     print(y)
