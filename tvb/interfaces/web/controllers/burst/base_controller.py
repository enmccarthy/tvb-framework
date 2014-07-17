# -*- coding: utf-8 -*-
#
#
# TheVirtualBrain-Framework Package. This package holds all Data Management, and 
# Web-UI helpful to run brain-simulations. To use it, you also need do download
# TheVirtualBrain-Scientific Package (for simulators). See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
# CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
module docstring
.. moduleauthor:: Mihai Andrei <mihai.andrei@codemart.ro>
"""
from tvb.interfaces.web.controllers import common
from tvb.interfaces.web.controllers.base_controller import BaseController


class BurstBaseController(BaseController):

    def fill_default_attributes(self, template_dictionary, subsection='burst'):
        template_dictionary[common.KEY_SECTION] = 'burst'
        template_dictionary[common.KEY_SUB_SECTION] = subsection
        template_dictionary[common.KEY_SUBMENU_LIST] = [
            {'link' : '/burst', 'subsection': 'burst',
             'title' : 'Simulation Cockpit', 'description':'Manage simulations'},
            {'link' : '/burst/dynamic', 'subsection': 'dynamic',
             'title' : 'Model configurations', 'description':'Create model configurations'}
        ]
        template_dictionary[common.KEY_PARAMETERS_CONFIG] = False

        BaseController.fill_default_attributes(self, template_dictionary)
        return template_dictionary

    @staticmethod
    def group_parameter_values_by_name(model_parameters_list):
        """
        Given a list of model parameters like this:
            ["a", [2.0]], ['b', [1.0]
            ["a", [3.0]], ['b', [7.0]
        Group them by param name to get:
        {'a': [2.0, 3.0], 'b': [1.0, 7.0]}
        """
        ret = {}
        for model_parameters in model_parameters_list:
            for param_name, param_vals in model_parameters:
                if param_name not in ret:
                    ret[param_name] = []
                ret[param_name].extend(param_vals)
        return ret