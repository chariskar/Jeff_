"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var Nations_1 = require("./src/Nations");
var Players_1 = require("./src/Players");
var Towns_1 = require("./src/Towns");
var Discord = require("discord.js");
var dotenv = require("dotenv");
var sends_1 = require("./src/utils/sends");
var weather_1 = require("./src/weather");
var client = new Discord.Client();
var Send = new sends_1.send(client);
var nationCommand = new Nations_1.Nations(client, Send);
var townCommand = new Towns_1.TownCommand(client, Send);
var playerCommand = new Players_1.playercommand(client, Send);
var weathercommand = new weather_1.Weather(client, Send);
dotenv.config();
client.on('message', function (message) { return __awaiter(void 0, void 0, void 0, function () {
    var args, command, subCommand, subCommand, subCommand, subCommand;
    var _a, _b, _c, _d, _e;
    return __generator(this, function (_f) {
        switch (_f.label) {
            case 0:
                if (message.author.bot)
                    return [2 /*return*/];
                args = message.content.split(' ');
                command = (_a = args.shift()) === null || _a === void 0 ? void 0 : _a.toLowerCase();
                if (!(command === '/nation')) return [3 /*break*/, 17];
                subCommand = (_b = args[0]) === null || _b === void 0 ? void 0 : _b.toLowerCase();
                if (!(subCommand === 'search')) return [3 /*break*/, 2];
                return [4 /*yield*/, nationCommand.search(args[1], args[2])];
            case 1:
                _f.sent();
                return [3 /*break*/, 16];
            case 2:
                if (!(subCommand === 'reslist')) return [3 /*break*/, 4];
                return [4 /*yield*/, nationCommand.reslist(args[1], args[2])];
            case 3:
                _f.sent();
                return [3 /*break*/, 16];
            case 4:
                if (!(subCommand === 'ranklist')) return [3 /*break*/, 6];
                return [4 /*yield*/, nationCommand.ranklist(args[1], args[2])];
            case 5:
                _f.sent();
                return [3 /*break*/, 16];
            case 6:
                if (!(subCommand === 'allylist')) return [3 /*break*/, 8];
                return [4 /*yield*/, nationCommand.allylist(args[1], args[2])];
            case 7:
                _f.sent();
                return [3 /*break*/, 16];
            case 8:
                if (!(subCommand === 'enemylist')) return [3 /*break*/, 10];
                return [4 /*yield*/, nationCommand.enemylist(args[1], args[2])];
            case 9:
                _f.sent();
                return [3 /*break*/, 16];
            case 10:
                if (!(subCommand === 'townlist')) return [3 /*break*/, 12];
                return [4 /*yield*/, nationCommand.townlist(args[1], args[2])];
            case 11:
                _f.sent();
                return [3 /*break*/, 16];
            case 12:
                if (!(subCommand === 'unallied')) return [3 /*break*/, 14];
                return [4 /*yield*/, nationCommand.unallied(args[1], args[2])];
            case 13:
                _f.sent();
                return [3 /*break*/, 16];
            case 14: return [4 /*yield*/, nationCommand.nation()];
            case 15:
                _f.sent();
                _f.label = 16;
            case 16: return [3 /*break*/, 33];
            case 17:
                if (!(command === '/town')) return [3 /*break*/, 24];
                subCommand = (_c = args[0]) === null || _c === void 0 ? void 0 : _c.toLowerCase();
                if (!(subCommand === 'search')) return [3 /*break*/, 19];
                return [4 /*yield*/, townCommand.search(args[1])];
            case 18:
                _f.sent();
                return [3 /*break*/, 23];
            case 19:
                if (!(subCommand === 'rank')) return [3 /*break*/, 21];
                return [4 /*yield*/, townCommand.ranklist(args[1])];
            case 20:
                _f.sent();
                return [3 /*break*/, 23];
            case 21:
                if (!(subCommand === 'ranklist')) return [3 /*break*/, 23];
                return [4 /*yield*/, townCommand.ranklist(args[1])];
            case 22:
                _f.sent();
                _f.label = 23;
            case 23: return [3 /*break*/, 33];
            case 24:
                if (!(command === '/player')) return [3 /*break*/, 31];
                subCommand = (_d = args[0]) === null || _d === void 0 ? void 0 : _d.toLowerCase();
                if (!(subCommand === 'search')) return [3 /*break*/, 26];
                return [4 /*yield*/, playerCommand.search(args[1])];
            case 25:
                _f.sent();
                return [3 /*break*/, 30];
            case 26:
                if (!(subCommand === 'friendlist')) return [3 /*break*/, 28];
                return [4 /*yield*/, playerCommand.friendlist(args[1])];
            case 27:
                _f.sent();
                return [3 /*break*/, 30];
            case 28:
                if (!(subCommand === 'rank')) return [3 /*break*/, 30];
                return [4 /*yield*/, playerCommand.rank(args[1], args[2])];
            case 29:
                _f.sent();
                _f.label = 30;
            case 30: return [3 /*break*/, 33];
            case 31:
                if (!(command === '/weather')) return [3 /*break*/, 33];
                subCommand = (_e = args[0]) === null || _e === void 0 ? void 0 : _e.toLowerCase();
                if (!(subCommand === '/weather search')) return [3 /*break*/, 33];
                return [4 /*yield*/, weathercommand.search(args[1])];
            case 32:
                _f.sent();
                _f.label = 33;
            case 33: return [2 /*return*/];
        }
    });
}); });
try {
    var token = process.env.TOKEN;
    client.login(token);
}
catch (e) {
    throw new console.error("Error " + e);
}
