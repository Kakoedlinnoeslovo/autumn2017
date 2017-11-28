var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

try {
    var devServerConfig = require('./devserver.local.config');
} catch (ex) {
    var devServerConfig = require('./devserver.base.config');
}

module.exports = {
    context: __dirname,

    devtool: 'source-map',

    entry: {
        presentation: [
            './static/js/presentation/index.es6',
        ],
        constructor: [
            './static/js/constructor/index.es6',
        ],
        base: [
            './static/css/elements.css',
            './static/css/presentation.css',
            './static/js/base.es6',
        ]
    },

    output: {
        path: path.resolve('./static/dist/'),
        filename: '[name][chunkhash].entry.js',

        // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
        publicPath: devServerConfig.publicPath
    },

    plugins: [
        new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js', Infinity),
        new BundleTracker({ filename: './webpack-stats.json' })
    ],

    module: {
        loaders: [
            {
                test: /\.(jsx?|es6)$/,
                exclude: [
                    /node_modules/,
                ],
                loader: 'babel',
                query: {
                    presets:['es2015', 'react']
                }
            },
            {
                test: /\.css$/,
                loaders: [
                    'style',
                    'css',
                ],
            },
        ]
    },

    resolve: {
        root: __dirname + '/static',
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.es6', '.js', '.jsx']
    },
};
