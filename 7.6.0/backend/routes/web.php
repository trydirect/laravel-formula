<?php

use Illuminate\Support\Facades\Request;
use \Illuminate\Support\Facades\Route;
use Jippi\Vault\Client as VaultClient;
use Illuminate\Support\Facades\Redis;
use Predis\Connection\ConnectionException;
use PhpAmqpLib\Connection\AMQPStreamConnection;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/test', function (Request $request) {
    return "Hello World!";
});

Route::get('/vault/get', function (Request $request) {
    try {
        $client = new VaultClient();
        $status = (string) $client->get('v1/secret/test')->getBody();
        return "Ok";
    } catch (Exception $e) {
        return $e->getMessage();
    }
});

Route::get('/redis/connect', function () {
    try {
        $redis = Redis::connection();
        $redis->ping();
        return response('Connected!');
    } catch (ConnectionException $e) {
        return $e->getMessage();
    }
});

Route::get('/rabbit/connect', function () {
    $host = getenv('RABBIT_HOST');
    $port = (int) getenv('RABBIT_PORT');
    $user = getenv('RABBIT_LOGIN');
    $password = getenv('RABBIT_PASSWORD');
    $vhost = getenv('RABBIT_VHOST');
    try {
        $connect = new AMQPStreamConnection($host, $port, $user, $password, $vhost);
        return response('Connected!');
    } catch (Exception $e) {
        return $e->getMessage();
    }
});