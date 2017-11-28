var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.config');
delete config.entry.hmr;
config.devtool = undefined;
config.output.publicPath = '/static/dist/';
config.plugins = [
    new webpack.DefinePlugin({
        'process.env': {
            NODE_ENV: JSON.stringify('production'),
        },
    }),
    new webpack.optimize.UglifyJsPlugin({
        compress: {
            warnings: false,
        },
    }),
    new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.js', Infinity),
    new BundleTracker({ filename: './webpack-stats.json' }),
];
module.exports = config;
