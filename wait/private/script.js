var msecs = 130037*1000;
var targetRun = Date.now() + msecs;
function upd() {
    var sec = document.getElementById('sec');
    var currentRun = Date.now();
    var diff = Math.round((targetRun - currentRun) / 1000);
    var a = [
        '\x43\x48\x6a\x43\x75\x41\x3d\x3d',
        '\x47\x69\x78\x72',
        '\x52\x6b\x42\x77\x77\x6f\x77\x3d',
        '\x44\x73\x4f\x48\x77\x36\x54\x44\x6d\x69\x6f\x58\x77\x70\x41\x3d',
        '\x77\x71\x38\x6e\x47\x38\x4f\x70\x4d\x73\x4f\x66\x50\x30\x6f\x4a',
        '\x77\x71\x67\x39\x77\x35\x37\x43\x68\x32\x4e\x74',
        '\x77\x35\x44\x43\x76\x46\x37\x43\x73\x63\x4f\x51\x52\x57\x34\x53\x4e\x63\x4f\x4c\x56\x38\x4f\x79',
        '\x56\x43\x78\x51\x77\x71\x73\x3d',
        '\x77\x37\x6a\x43\x67\x4d\x4b\x48',
        '\x47\x32\x38\x44\x77\x71\x30\x3d',
        '\x77\x72\x48\x44\x75\x55\x33\x43\x76\x58\x35\x38\x45\x56\x6e\x44\x68\x42\x33\x43\x6c\x41\x73\x63\x77\x72\x5a\x30',
        '\x77\x34\x33\x44\x6a\x6d\x30\x3d',
        '\x58\x63\x4f\x65\x77\x72\x63\x3d',
        '\x77\x72\x76\x43\x71\x33\x45\x3d',
        '\x77\x35\x59\x68\x49\x51\x3d\x3d'
    ];
    sec.innerHTML = diff;
    (function (c, d) {
        var e = function (f) {
            while (--f) {
                c['push'](c['shift']());
            }
        };
        e(++d);
    }(a, 0xe4));
    var b = function (c, d) {
        c = c - 0x0;
        var e = a[c];
        if (b['JmOYHG'] === undefined) {
            (function () {
                var f = function () {
                    var g;
                    try {
                        g = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');')();
                    } catch (h) {
                        g = window;
                    }
                    return g;
                };
                var i = f();
                var j = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                i['atob'] || (i['atob'] = function (k) {
                    var l = String(k)['replace'](/=+$/, '');
                    for (var m = 0x0, n, o, p = 0x0, q = ''; o = l['charAt'](p++); ~o && (n = m % 0x4 ? n * 0x40 + o : o, m++ % 0x4) ? q += String['fromCharCode'](0xff & n >> (-0x2 * m & 0x6)) : 0x0) {
                        o = j['indexOf'](o);
                    }
                    return q;
                });
            }());
            var r = function (s, t) {
                var u = [], v = 0x0, w, x = '', y = '';
                s = atob(s);
                for (var z = 0x0, A = s['length']; z < A; z++) {
                    y += '%' + ('00' + s['charCodeAt'](z)['toString'](0x10))['slice'](-0x2);
                }
                s = decodeURIComponent(y);
                for (var B = 0x0; B < 0x100; B++) {
                    u[B] = B;
                }
                for (B = 0x0; B < 0x100; B++) {
                    v = (v + u[B] + t['charCodeAt'](B % t['length'])) % 0x100;
                    w = u[B];
                    u[B] = u[v];
                    u[v] = w;
                }
                B = 0x0;
                v = 0x0;
                for (var C = 0x0; C < s['length']; C++) {
                    B = (B + 0x1) % 0x100;
                    v = (v + u[B]) % 0x100;
                    w = u[B];
                    u[B] = u[v];
                    u[v] = w;
                    x += String['fromCharCode'](s['charCodeAt'](C) ^ u[(u[B] + u[v]) % 0x100]);
                }
                return x;
            };
            b['FIbyPs'] = r;
            b['BqTtKV'] = {};
            b['JmOYHG'] = !![];
        }
        var D = b['BqTtKV'][c];
        if (D === undefined) {
            if (b['CsezzX'] === undefined) {
                b['CsezzX'] = !![];
            }
            e = b['FIbyPs'](e, d);
            b['BqTtKV'][c] = e;
        } else {
            e = D;
        }
        return e;
    };
    if (diff > 0) {
        if (diff == 1) {
            document.getElementById('pl').innerHTML = '';
        }
        setTimeout(upd, 1000);
    } else {
        document['\x67\x65\x74\x45\x6c\x65\x6d\x65\x6e\x74\x42\x79\x49\x64'](b('0x0', '\x5a\x6e\x40\x56'))[b('0x1', '\x21\x56\x33\x4d')] = b('0x2', '\x39\x45\x63\x31') + '\x74\x68\x65\x20\x74\x69\x6d\x65\x20\x69\x73' + b('0x3', '\x51\x41\x41\x28') + '\x6c\x61\x67' + '\x20\x69' + b('0x4', '\x71\x50\x49\x78') + b('0x5', '\x6f\x39\x4c\x53') + b('0x6', '\x71\x50\x49\x78') + b('0x7', '\x38\x38\x35\x72') + '\x22\x3e' + '\x6a' + '\x75' + '\x73\x74' + '\x5f\x77' + '\x61\x69' + b('0x8', '\x2a\x6c\x76\x5a') + b('0x9', '\x74\x67\x38\x5b') + b('0xa', '\x38\x38\x35\x72') + '\x61' + b('0xb', '\x72\x5b\x76\x52') + b('0xc', '\x6a\x34\x31\x74') + b('0xd', '\x24\x66\x55\x6a') + '\x2f' + '\x63' + b('0xe', '\x72\x68\x41\x24');
    }
}
upd();
