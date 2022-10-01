import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    # Definicion de 5 casos de prueba 
    def test_crear_znode_ephemeral(self):
        tree = Ztree()
        # create(self,path,data,ephemeral,OnService,timeDead,parent
        tree.create('/node1','algo',True,True,10,'/')
        self.assertTrue(tree.getData('/node1'),'algo')

    def test_borrar_znode_ephemeral(self):
        tree = Ztree()
        tree.create('/node1','algo',True,True,5,'/')
        tree.delete('/node1',5)
        self.assertFalse(tree.exist('/node1'))

    def test_cambiar_datos(self):
        tree = Ztree()
        tree.create('/node1','algo',True,True,10,'/')
        tree.setData('/node1','something')
        self.assertEqual(tree.getData('/node1'),'algo') # Fallara porque something != algo

    def test_buscar_znode_ephemeral(self):
        tree = Ztree()
        tree.create('/node1','algo',True,False,5,'/')
        self.assertTrue(tree.exist('/node1'))

    def test_znode_None(self):
        tree = Ztree()
        tree.create('/node1','algo',False,True,10,'/')
        self.assertIsNotNone(tree)



if __name__ == '__main__':
    unittest.main()

