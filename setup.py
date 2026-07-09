# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='segale',
    version='0.1.0',
    py_modules=['segale_align', 'segale_eval'],
    packages=find_packages(),
    install_requires=[
        'spacy==3.8.14',
        'torch==2.12.0',
        'numpy==1.26.4',
        'pandas==2.2.3',
        'tqdm==4.67.1',
        'transformers==4.51.3',
        'unbabel-comet==2.2.7',
        'vecalign @ git+https://github.com/thompsonb/vecalign@v2.0.0',
        # Forked from facebookresearch/LASER: fairseq removed from install_requires,
        # fairseq imports wrapped in try/except so the module loads without fairseq
        # (which conflicts with python>=3.10)
        'laser-encoders @ git+https://github.com/jeffwillette/LASER.git@14ba8c31efe48c351333ff0159fe2d25a6aaee37',
    ],
    entry_points={
        'console_scripts': [
            'segale-align = segale_align:main',
            'segale-eval = segale_eval:main',
        ],
    },
)
