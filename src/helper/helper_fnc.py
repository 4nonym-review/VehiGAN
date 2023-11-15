from omegaconf import OmegaConf
from omegaconf import DictConfig


def construct_model_cfg(cfg:any)->list:
    model_param = []
    print("cfg.models: ", cfg.models)
    model_configs = cfg.models
    model_type = model_configs["model_type"]          
        
    if model_type == 'autoencoder':
        for num_hid_layers in model_configs.list_of_num_hid_layers:
            for max_epoch in model_configs.list_of_max_epoch:
                model_cfg = {
                    "model_type" : 'autoencoder',
                    "num_hid_layers": num_hid_layers,
                    'max_epoch' : max_epoch
                    }
                model_param.append(OmegaConf.create(model_cfg))

    
    elif model_type =='wgan':
        for num_hid_layers in model_configs.list_of_num_hid_layers:
            for noise_dim in model_configs.list_of_noise_dim:
                for max_epoch in model_configs.list_of_max_epoch:
                    model_cfg = {
                        "model_type" : 'wgan',
                        "num_hid_layers": num_hid_layers,
                        "noise_dim": noise_dim,
                        'max_epoch' : max_epoch,
                        'gen_sample_size' : model_configs.gen_sample_size
                        }
                    model_param.append(OmegaConf.create(model_cfg))
    return model_param
