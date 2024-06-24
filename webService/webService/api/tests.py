from django.test import TestCase
from django.urls import reverse
from app.models import *
from .serializers import *
    

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create(**self.user_data)
        self.serializer = UserSerializer(instance=self.user)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user_data['username'])
        self.assertEqual(data['email'], self.user_data['email'])

    def test_deserialization(self):
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])

class ProductoSerializerTestCase(TestCase):
    def setUp(self):
        self.producto_data = {
            'nombre_producto': 'Producto de prueba',
            'precio': 10990,
            'cantidad': 5,
            'marca':'taladrin',
            'descripcion':'taladro para taladrar'
        }
        self.producto = Producto.objects.create(**self.producto_data)
        self.serializer = ProductoSerializer(instance=self.producto)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['nombre_producto'], self.producto_data['nombre_producto'])
        self.assertEqual(data['precio'], self.producto_data['precio'])
        self.assertEqual(data['cantidad'], self.producto_data['cantidad'])
        self.assertEqual(data['marca'], self.producto_data['marca'])
        self.assertEqual(data['descripcion'], self.producto_data['descripcion'])

    def test_deserialization(self):
        data = {
            'nombre_producto': 'martillo',
            'precio': 16000,
            'cantidad': 5,
            'marca':'taladrin',
            'descripcion':'martillo martillin'
        }
        serializer = ProductoSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        producto = serializer.save()
        self.assertEqual(producto.nombre_producto, data['nombre_producto'])
        self.assertEqual(producto.precio, data['precio'])
        self.assertEqual(producto.cantidad, data['cantidad'])
        self.assertEqual(producto.marca, data['marca'])
        self.assertEqual(producto.descripcion, data['descripcion'])

class EstadoSerializerTestCase(TestCase):
    def setUp(self):
        self.estado_data = {
            'nombre': 'Estado de prueba',
        }
        self.estado = Estado.objects.create(**self.estado_data)
        self.serializer = EstadoSerializer(instance=self.estado)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['nombre'], self.estado_data['nombre'])

class PedidoSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.cliente_data = {
            'user': self.user,
            'nombre': 'Cliente de prueba',
            'email': 'tG3Rn@example.com',
            'direccion':'mi casa 1234'
        }
        self.cliente = Cliente.objects.create(**self.cliente_data)

        self.estado_data = {
            'nombre': 'Estado de prueba',
        }
        self.estado = Estado.objects.create(**self.estado_data)

        self.pedido_data = {
            'cliente': self.cliente,
            'estado': self.estado,
            'subtotal': 10990,
            'iva': 19,
            'total': 10990
        }
        self.pedido = Pedido.objects.create(**self.pedido_data)
        self.serializer = PedidoSerializer(instance=self.pedido)

    def test_serialization(self):
        data = self.serializer.data
        # Verifica que los datos serializados sean correctos
        self.assertEqual(data['cliente']['nombre'], self.cliente_data['nombre'])
        self.assertEqual(data['estado']['nombre'], self.estado_data['nombre'])


class InvalidUserSerializerTestCase(TestCase):

    def test_user_serializer_invalid_data(self):
        # Datos inválidos: el campo 'username' está vacío y el 'email' tiene un formato incorrecto
        invalid_data = {
            'username': '',
            'email': 'invalidemail',
            'password': 'testpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)
        self.assertIn('email', serializer.errors)

if __name__ == '__main__':
    unittest.main()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True}
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class WeakPasswordSerializerTestCase(TestCase):

    def test_user_serializer_weak_password(self):
        # Datos inválidos: el campo 'password' es demasiado corto
        invalid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': 'short'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('password', serializer.errors)

if __name__ == '__main__':
    unittest.main()


class DuplicateUsernameSerializerTestCase(TestCase):

    def setUp(self):
        # Crear un usuario con un nombre de usuario específico
        self.existing_user = User.objects.create_user(
            username='existinguser', 
            email='existinguser@example.com', 
            password='testpassword'
        )

    def test_user_serializer_duplicate_username(self):
        # Datos inválidos: el nombre de usuario ya existe
        invalid_data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password': 'testpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)

if __name__ == '__main__':
    unittest.main()



class MissingFieldsSerializerTestCase(TestCase):

    def test_user_serializer_missing_fields(self):
        # Datos inválidos: el campo 'email' está ausente
        invalid_data = {
            'username': 'validusername',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)

    def test_user_serializer_missing_all_fields(self):
        # Datos inválidos: todos los campos están ausentes
        invalid_data = {}
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)

if __name__ == '__main__':
    unittest.main()

class InvalidEmailFormatSerializerTestCase(TestCase):

    def test_user_serializer_invalid_email_format(self):
        # Datos inválidos: el campo 'email' tiene un formato incorrecto
        invalid_data = {
            'username': 'validusername',
            'email': 'invalidemail',
            'password': 'testpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)

if __name__ == '__main__':
    unittest.main()

class MissingUsernameSerializerTestCase(TestCase):

    def test_user_serializer_missing_username(self):
        # Datos inválidos: el campo 'username' está ausente
        invalid_data = {
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class MissingPasswordSerializerTestCase(TestCase):

    def test_user_serializer_missing_password(self):
        # Datos inválidos: el campo 'password' está ausente
        invalid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('password', serializer.errors)


class UsernameWithSpacesSerializerTestCase(TestCase):

    def test_user_serializer_username_with_spaces(self):
        # Datos inválidos: el campo 'username' contiene espacios
        invalid_data = {
            'username': 'user name',
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


        


class PasswordAllSpacesSerializerTestCase(TestCase):

    def test_user_serializer_password_all_spaces(self):
        # Datos inválidos: el campo 'password' contiene solo espacios
        invalid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': '        '
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('password', serializer.errors)

class ValidUserSerializerTestCase(TestCase):

    def test_user_serializer_valid_data(self):
        # Datos válidos: todos los campos son correctos
        valid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        self.assertNotIn('username', serializer.errors)
        self.assertNotIn('email', serializer.errors)
        self.assertNotIn('password', serializer.errors)


class EmailWithoutDomainSerializerTestCase(TestCase):

    def test_user_serializer_email_without_domain(self):
        # Datos inválidos: el campo 'email' no tiene dominio
        invalid_data = {
            'username': 'validusername',
            'email': 'email@',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)

class LongUsernameSerializerTestCase(TestCase):

    def test_user_serializer_long_username(self):
        # Datos inválidos: el campo 'username' es demasiado largo
        invalid_data = {
            'username': 'a' * 151,  # Suponiendo que el máximo permitido es 150 caracteres
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class EmailWithoutAtSymbolSerializerTestCase(TestCase):

    def test_user_serializer_email_without_at_symbol(self):
        # Datos inválidos: el campo 'email' no contiene el símbolo '@'
        invalid_data = {
            'username': 'validusername',
            'email': 'email.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)


class UsernameWithSpecialCharsSerializerTestCase(TestCase):

    def test_user_serializer_username_with_special_chars(self):
        # Datos inválidos: el campo 'username' contiene caracteres especiales
        invalid_data = {
            'username': 'username!',
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class UsernameAlreadyExistsSerializerTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='existinguser', email='existinguser@example.com', password='existingpassword')

    def test_user_serializer_username_already_exists(self):
        # Datos inválidos: el campo 'username' ya existe en la base de datos
        invalid_data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password': 'newpassword'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class EmailWithSubdomainSerializerTestCase(TestCase):

    def test_user_serializer_email_with_subdomain(self):
        # Datos válidos: el campo 'email' contiene un subdominio
        valid_data = {
            'username': 'validusername',
            'email': 'email@subdomain.example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class UsernameWithNumbersSerializerTestCase(TestCase):

    def test_user_serializer_username_with_numbers(self):
        # Datos válidos: el campo 'username' contiene números
        valid_data = {
            'username': 'user1234',
            'email': 'validemail@example.com',
            'password': 'validpassword'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class EmailWithSpecialCharsSerializerTestCase(TestCase):

    def test_user_serializer_email_with_special_chars(self):
        # Datos válidos: el campo 'email' contiene caracteres especiales válidos
        valid_data = {
            'username': 'validusername',
            'email': 'valid.email+alias@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class EmailWithoutTLDSerializerTestCase(TestCase):

    def test_user_serializer_email_without_tld(self):
        # Datos inválidos: el campo 'email' no contiene un TLD
        invalid_data = {
            'username': 'validusername',
            'email': 'email@domain',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)


class UsernameWithUnderscoresSerializerTestCase(TestCase):

    def test_user_serializer_username_with_underscores(self):
        # Datos válidos: el campo 'username' contiene guiones bajos
        valid_data = {
            'username': 'valid_username',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class UsernameWithDotsSerializerTestCase(TestCase):

    def test_user_serializer_username_with_dots(self):
        # Datos válidos: el campo 'username' contiene puntos
        valid_data = {
            'username': 'valid.username',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class EmailWithMultipleDomainExtensionsSerializerTestCase(TestCase):

    def test_user_serializer_email_with_multiple_domain_extensions(self):
        # Datos válidos: el campo 'email' tiene múltiples extensiones de dominio
        valid_data = {
            'username': 'validusername',
            'email': 'email@domain.co.uk',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class LocalDomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_local_domain_email(self):
        # Datos válidos: el campo 'email' contiene un nombre de dominio local
        valid_data = {
            'username': 'validusername',
            'email': 'email@localhost',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class InternationalizedDomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_internationalized_domain_email(self):
        # Datos válidos: el campo 'email' contiene un dominio internacionalizado
        valid_data = {
            'username': 'validusername',
            'email': 'email@xn--bcher-kva.example',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class TopLevelDomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_top_level_domain_email(self):
        # Datos válidos: el campo 'email' contiene etiquetas de dominio superior
        valid_data = {
            'username': 'validusername',
            'email': 'email@domain.travel',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class LongSubdomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_long_subdomain_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio largo
        valid_data = {
            'username': 'validusername',
            'email': 'email@sub.sub.sub.sub.sub.domain.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)



class EmailWithDomainWithoutDotSerializerTestCase(TestCase):

    def test_user_serializer_email_with_domain_without_dot(self):
        # Datos inválidos: el campo 'email' tiene un nombre de dominio sin un punto
        invalid_data = {
            'username': 'validusername',
            'email': 'email@domain',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)


class MaxLengthUsernameSerializerTestCase(TestCase):

    def test_user_serializer_max_length_username(self):
        # Datos válidos: el campo 'username' tiene la longitud máxima permitida
        valid_data = {
            'username': 'a' * 150,
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class EmailWithQuotesSerializerTestCase(TestCase):

    def test_user_serializer_email_with_quotes(self):
        # Datos válidos: el campo 'email' contiene comillas
        valid_data = {
            'username': 'validusername',
            'email': '"email"@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class EmailWithDoubleAtSerializerTestCase(TestCase):

    def test_user_serializer_email_with_double_at(self):
        # Datos inválidos: el campo 'email' contiene doble arroba
        invalid_data = {
            'username': 'validusername',
            'email': 'email@@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)



class SubdomainAndDotLocalPartEmailSerializerTestCase(TestCase):

    def test_user_serializer_subdomain_and_dot_local_part_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio y un punto en el nombre local
        valid_data = {
            'username': 'validusername',
            'email': 'first.last@sub.domain.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class MixedCharsUsernameSerializerTestCase(TestCase):

    def test_user_serializer_mixed_chars_username(self):
        # Datos válidos: el campo 'username' contiene una mezcla de caracteres permitidos
        valid_data = {
            'username': 'user_name-123',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class NumberedSubdomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_numbered_subdomain_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio numerado
        valid_data = {
            'username': 'validusername',
            'email': 'email@123.domain.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class SpecialCharsUsernameSerializerTestCase(TestCase):

    def test_user_serializer_special_chars_username(self):
        # Datos inválidos: el campo 'username' contiene caracteres especiales
        invalid_data = {
            'username': '!username#',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class MaxLengthEmailSerializerTestCase(TestCase):

    def test_user_serializer_max_length_email(self):
        # Datos inválidos: el campo 'email' tiene la longitud máxima permitida
        invalid_data = {
            'username': 'validusername',
            'email': 'a' * 243 + '@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('email', serializer.errors)


class MinLengthPasswordSerializerTestCase(TestCase):

    def test_user_serializer_min_length_password(self):
        # Datos inválidos: el campo 'password' tiene la longitud mínima permitida
        invalid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': 'Pass1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('password', serializer.errors)


class UnicodeUsernameSerializerTestCase(TestCase):

    def test_user_serializer_unicode_username(self):
        # Datos válidos: el campo 'username' contiene caracteres unicode
        valid_data = {
            'username': 'üsername123',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class SubdomainUnderscoreEmailSerializerTestCase(TestCase):

    def test_user_serializer_subdomain_underscore_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio con guión bajo
        valid_data = {
            'username': 'validusername',
            'email': 'first_last@sub.example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class MixedCaseAndNumberPasswordSerializerTestCase(TestCase):

    def test_user_serializer_mixed_case_and_number_password(self):
        # Datos válidos: el campo 'password' contiene mayúsculas, minúsculas y números
        valid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': 'MixedCase1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class NumericOnlyUsernameSerializerTestCase(TestCase):

    def test_user_serializer_numeric_only_username(self):
        # Datos válidos: el campo 'username' contiene solo números
        valid_data = {
            'username': '1234567890',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class UppercaseSubdomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_uppercase_subdomain_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio en mayúsculas
        valid_data = {
            'username': 'validusername',
            'email': 'user@SUB.example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class AllowedSpecialCharsPasswordSerializerTestCase(TestCase):

    def test_user_serializer_allowed_special_chars_password(self):
        # Datos válidos: el campo 'password' contiene caracteres especiales permitidos
        valid_data = {
            'username': 'validusername',
            'email': 'validemail@example.com',
            'password': '!Password123$'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class NumericSubdomainAndHyphenEmailSerializerTestCase(TestCase):

    def test_user_serializer_numeric_subdomain_and_hyphen_email(self):
        # Datos válidos: el campo 'email' contiene un subdominio numérico y guiones
        valid_data = {
            'username': 'validusername',
            'email': 'user@123-domain.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class AlphanumericUnderscoreUsernameSerializerTestCase(TestCase):

    def test_user_serializer_alphanumeric_underscore_username(self):
        # Datos válidos: el campo 'username' contiene caracteres alfanuméricos y guiones bajos
        valid_data = {
            'username': 'user_name123',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class InvalidSpecialCharsUsernameSerializerTestCase(TestCase):

    def test_user_serializer_invalid_special_chars_username(self):
        # Datos inválidos: el campo 'username' contiene caracteres especiales no permitidos
        invalid_data = {
            'username': 'user$name',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=invalid_data)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        self.assertIn('username', serializer.errors)


class UppercaseDomainEmailSerializerTestCase(TestCase):

    def test_user_serializer_uppercase_domain_email(self):
        # Datos válidos: el campo 'email' tiene el dominio en mayúsculas
        valid_data = {
            'username': 'validusername',
            'email': 'user@EXAMPLE.COM',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)


class LowercaseLettersUsernameSerializerTestCase(TestCase):

    def test_user_serializer_lowercase_letters_username(self):
        # Datos válidos: el campo 'username' contiene solo letras minúsculas
        valid_data = {
            'username': 'lowercase',
            'email': 'validemail@example.com',
            'password': 'validPassword1!'
        }
        serializer = UserSerializer(data=valid_data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
