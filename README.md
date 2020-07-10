# get-roam-repo
Get Roam Repo (grr) converts a GitHub repository's file-structure into Markdown for taking notes with Roam Research.

The program will print the result and save it to your clipboard. The output is originally intended to be for pasting into Roam.

`python main.py --repo shawwn/stylegan2`

becomes

<img src="https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FNoa%2Fh1ybXwsQDd.png?alt=media&token=29f4481d-74b2-43a2-bd2c-407bfa2c9fba" width="60%">

or in raw text form

```
- ### docs
    - **stylegan2-training-curves.png**
    - **license.html**
    - **stylegan2-teaser-1024x256.png**
    - **versions.html**
- ### training
    - **networks_stylegan2.py**
    - **misc.py**
    - **networks_stylegan.py**
    - **loss.py**
    - $$\_\_$$**init**$$\_\_$$**.py**
    - **dataset.py**
    - **training_loop.py**
- ### dnnlib
    - ### submission
        - ### internal
            - $$\_\_$$**init**$$\_\_$$**.py**
            - **local.py**
        - **submit.py**
        - **run_context.py**
        - $$\_\_$$**init**$$\_\_$$**.py**
    - ### tflib
        - ### ops
            - **upfirdn_2d.cu**
            - **upfirdn_2d.py**
            - $$\_\_$$**init**$$\_\_$$**.py**
            - **fused_bias_act.py**
            - **fused_bias_act.cu**
        - **tfutil.py**
        - **autosummary.py**
        - $$\_\_$$**init**$$\_\_$$**.py**
        - **optimizer.py**
        - **custom_ops.py**
        - **network.py**
    - **util.py**
    - $$\_\_$$**init**$$\_\_$$**.py**
- ### metrics
    - **metric_defaults.py**
    - **frechet_inception_distance.py**
    - **linear_separability.py**
    - **metric_base.py**
    - **perceptual_path_length.py**
    - **precision_recall.py**
    - **inception_score.py**
    - $$\_\_$$**init**$$\_\_$$**.py**
- **Dockerfile**
- **run_metrics.py**
- **test_nvcc.cu**
- **run_projector.py**
- **dataset_tool.py**
- **run_generator.py**
- **README.md**
- **LICENSE.txt**
- **run_training.py**
- **projector.py**
- **pretrained_networks.py**
```
