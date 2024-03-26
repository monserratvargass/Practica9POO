<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\BeastMexController;

use App\Http\Controllers\controladorAlmacen;
use App\Http\Controllers\controladorCompras;
use App\Http\Controllers\controladorGerencia;
use App\Http\Controllers\controladorVentas;
use App\Http\Controllers\AlmacenController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

/* Route::get('/', function () {
    return view('welcome');
}); */

Auth::routes();

Route::get('/home', [BeastMexController::class, 'index'])->middleware('auth');

//COMPRAS
Route::get('/', [BeastMexController::class, 'index'])->middleware('auth');

Route::get('/compraConsultarOrdenCompra', [controladorCompras::class, 'metodoConsultarOC'])->middleware('auth');


Route::get('/comprasBuscarProductos', [controladorCompras::class, 'metodoBuscarProductos'])->middleware('auth');


Route::get('/comprasRegistroProveedores', [controladorCompras::class, 'metodoRegistroProveedor'])->middleware('auth');


Route::post('/pBuscarProductos', [controladorCompras::class, 'metodoComprasBP'])->middleware('auth');

Route::post('/pRegistrarProveedor', [controladorCompras::class, 'metodoRegistroP'])->middleware('auth');

//ALMACEN
Route::get('/almacenRegistrarProducto',[controladorAlmacen::class,'metodoRegistroProducto'])->name('paginaActualizar')->middleware('auth');
Route::get('/almacenActualizar',[controladorAlmacen::class,'metodoActualizar'])->name('paginaActualizar')->middleware('auth');
Route::get('/almacenBuscar',[controladorAlmacen::class,'metodoBuscar'])->name('paginaBuscar')->middleware('auth');
Route::get('/almacenConsultar',[controladorAlmacen::class,'metodoConsultar'])->name('paginaConsultar')->middleware('auth');
Route::post('/guardarRegistro',[controladorAlmacen::class,'metodoGuardarAR'])->name('Guardar')->middleware('auth');
Route::post('/guardarRegistroAct',[controladorAlmacen::class,'metodoGuardarAct'])->name('GuardarAct')->middleware('auth');


Route::resource('productos',AlmacenController::class);


//VENTAS

//interfaz de ventas consultar productos
Route::get('/ventasConsultarproducto',[controladorVentas::class,'metodoMostrarproducto'])->name('Mostrarproducto')->middleware('auth');

Route::post('/Buscarproducto',[controladorVentas::class,'metodoBuscarproducto'])->name('Buscarproducto')->middleware('auth');

// interfaz de ventas resgistrar tickets
Route::get('/ventasRegistrartickets',[controladorVentas::class,'metodoRegistroVenta'])->name('Registroventa')->middleware('auth');

Route::post('/Guardartickets',[controladorVentas::class,'metodoGuardartickets'])->name('Guardartickets')->middleware('auth');

// interfaz de ventas calculo de ganancias
Route::get('/ventasCalculodeganancias',[controladorVentas::class,'metodoCalculodeganancias'])->name('Calculodeganancias')->middleware('auth');

Route::post('/Mostrarcalculodegancnias',[controladorVentas::class,'metodoMostrarcalculodegancnias'])->name('Mostrarcalculodegancnias')->middleware('auth');

// interfaz de ventas consultar tikets
Route::get('/ventasConsultartickets',[controladorVentas::class,'metodoConsultartickets'])->name('Consultartickets')->middleware('auth');

Route::post('/Mostrartickets',[controladorVentas::class,'metodoMostrartickets'])->name('Mostrartickets')->middleware('auth');
// imprimir tikets
Route::post('/Imprimirtickets',[controladorVentas::class,'metodoImprimirtickets'])->name('Imprimirtickets')->middleware('auth');


//GERENCIA

Route::get('/gerencia',[controladorGerencia::class,'metodoGerencia'])->name('Gerencia')->middleware('auth');
Route::post('/guardarU', [controladorGerencia::class, 'metodoGuardarUser'])->middleware('auth');

//seccion de reportes
Route::get('/gerenciaReportesVentas',[controladorGerencia::class,'metodoRV'])->middleware('auth');
Route::get('/gerenciaReportesGanancias',[controladorGerencia::class,'metodoRG'])->middleware('auth');
Route::get('/gerenciaReportesCompras',[controladorGerencia::class,'metodoRC'])->middleware('auth');

//registro y actualizar usuario

Route::get('/gerenciaRegistrarUsuario',[controladorGerencia::class,'metodoRegistrarU'])->middleware('auth');
Route::get('/gerenciaActualizarUsuario',[controladorGerencia::class,'metodoActualizarU'])->middleware('auth');

//consultar y buscar
Route::get('/gerenciaConsultarUsuario',[controladorGerencia::class,'metodoConsultarU'])->middleware('auth');
Route::get('/gerenciaBuscarUsuario',[controladorGerencia::class,'metodoBuscarU'])->middleware('auth');

/* Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home'); */