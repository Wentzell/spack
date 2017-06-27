##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Triqs(CMakePackage):
    """TRIQS: a Toolbox for Research on Interacting Quantum Systems"""

    # TRIQS Homepage and github page
    homepage = "https://triqs.ipht.cnrs.fr"
    url      = "https://github.com/TRIQS/triqs/archive/1.4.tar.gz"

    version('1.4', 'ca3c447993811b90b794f7ed57558556')
    version('master', git='https://github.com/TRIQS/triqs.git', branch='master')
    version('unstable', git='https://github.com/TRIQS/triqs.git', branch='unstable')

    # parallel = False

    # TRIQS Dependencies
    depends_on('gcc@4.9.1:', type=('build', 'link'))
    depends_on('gcc@5.1.0:', type=('build', 'link'), when='@unstable')
    depends_on('cmake@2.8.7:', type='build')
    depends_on('mpi', type=('build', 'link'))
    depends_on('lapack', type=('build', 'link'))
    depends_on('fftw@3.2.0:', type=('build', 'link'))
    depends_on('boost@1.49.0:', type=('build', 'link'))
    depends_on('hdf5@1.8.2:', type=('build', 'link'))
    # depends_on('llvm', type=('build', 'link'))
    depends_on('python@2.7.0:', type=('build', 'link', 'run'))
    depends_on('py-scipy')
    depends_on('py-numpy')
    depends_on('py-h5py')
    depends_on('py-matplotlib@0.99:')
    depends_on('py-mako@0.9.1:')
    depends_on('py-sphinx@1.0.1:')

    # def cmake_args(self):
        # # Specify arguments other than CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # args = []
        # return args
